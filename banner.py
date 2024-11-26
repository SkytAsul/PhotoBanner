import cv2 as cv
from pathlib import Path
import logging
import os
import numpy as np

logger = logging.getLogger(__name__)

# map of width to image
banners: dict[int, cv.typing.MatLike] = {}

def read_banner(banner_path: Path, desired_width: int):
    if desired_width in banners:
        return banners[desired_width]
    
    banner_img = cv.imread(str(banner_path))
    banner_shape = banner_img.shape
    banner_width = banner_shape[1]

    if banner_width != desired_width:
        factor = desired_width / banner_width
        banner_img = cv.resize(banner_img, None, fx=factor, fy=factor, interpolation=cv.INTER_LINEAR)
        logging.info("Resized banner from %dx%d to %dx%d", banner_shape[0], banner_shape[1], banner_img.shape[0], banner_img.shape[1])

    banners[desired_width] = banner_img
    return banner_img;

def process_img(from_path: Path, to_path: Path, banner_path: Path):
    if to_path.exists():
        logging.info("%s already processed.", to_path)
        return

    logging.info("Processing %s...", from_path)
    try:
        img = cv.imread(str(from_path))
        if img is None:
            logging.error("Cannot read image.")
            return
        
        banner_img = read_banner(banner_path, img.shape[1])
        
        # We simply append the banner to the image: it will automatically be at the end.
        img = np.append(img, banner_img, axis=0)

        if not to_path.parent.exists():
            to_path.parent.mkdir(parents=True)
        cv.imwrite(str(to_path), img)
    except Exception:
        logger.exception("Failed to process image")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(msecs)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")

    images_path = Path("images")
    processed_images_path = Path("imagesProcessed")
    banner_path = Path("banner.jpg")

    for root, dirs, files in os.walk(images_path):
        for file in files:
            img_path = Path(root, file)

            if not "." in img_path.name or img_path.name.index(".") == 0:
                # no extension or starts with dot: probably not an image to convert
                continue

            process_img(img_path, Path(processed_images_path, img_path.relative_to(images_path)), banner_path)

