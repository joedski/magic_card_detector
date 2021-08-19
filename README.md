# magic_card_detector

Python implementation of a Magic: the Gathering card segmentation and recognition

Still almost all Mikonen's work.  See their blog for more: https://tmikonen.github.io/quantitatively/2020-01-01-magic-card-detector/

## Dependencies

- Python ^3.7

Honestly, everything else is in the [`requirements.txt`](./requirements.txt).  Setup a virtual env and be happy!

Quick summary, though:

- ImageHash ^4.0
- NumPy ^1.17
- OpenCV 3.x (`python-opencv`)
    - NOTE: If you try running this and receive an error due to `cv2.findContours()` only returning 2 values instead of 3, you're using OpenCV 4.x, not 3.x!
- SciPi ^1.3
- Shapely ^1.6.4
