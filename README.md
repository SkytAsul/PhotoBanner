# PhotoBanner

This simple Python util automatically adds an image banner at the bottom of all your images at once.

## Installation

Either download or clone all of the repository locally and run
```bash
$ pip install -r requirements.txt
```

Otherwise, install `opencv-python` manually by calling
```bash
$ pip install opencv-python
```
and download the [`banner.py`](banner.py) file.

## Usage

Put all of your images in the `images` directory. You can put multiple folders here to keep a hierarchy.  
You must put your banner image in the root directory and name it `banner.jpg`. You can use another format, but you'll have to edit the `banner.py` file accordingly.

```
banner.py
banner.jpg
images
├── landscape.png
├── portraits
│   ├── portait1.jpg
│   └── portrait2.png
└── animals
    └── cat.jpg
```

Then, launch the Python file:
```bash
$ python3 banner.py

20:01:47:850.0 - INFO - Processing images/DSC01697.JPG...
20:01:48:202.0 - INFO - Resized banner from 147x1727 to 511x6000
20:01:48:819.0 - INFO - Processing images/random-pics/1673554186092.jpeg...
20:01:48:927.0 - INFO - Resized banner from 147x1727 to 184x2160
20:01:49:134.0 - INFO - Processing images/random-pics/2023wrapped_summary-share.jpeg...
20:01:49:157.0 - INFO - Resized banner from 147x1727 to 92x1080
...
```
You will find the pictures with banner added in the `imagesProcessed` folder.
