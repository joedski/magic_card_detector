import pickle
import magic_card_detector as mcg

# TODO: More than 1 set. (NOTE: would take ... awhile.  25+ years is a lot of cards.)
# REFERENCE_IMAGE_DIR = '../../MTG/Card_Images/LEA/'
# REFERENCE_IMAGE_DIR = '../../card-data/images/mtg/lea/'
REFERENCE_IMAGE_DIR = '../../card-data/mtg/images/lea/'
HASH_DATA_PATH = 'alpha_reference_phash.dat'

print('Hashing images in ' + REFERENCE_IMAGE_DIR)

card_detector = mcg.MagicCardDetector()
card_detector.read_and_adjust_reference_images(REFERENCE_IMAGE_DIR)

print('Hashed ' + str(len(card_detector.reference_images)) + ' images')

hlist = []
for image in card_detector.reference_images:
    image.original = None
    image.clahe = None
    image.adjusted = None
    hlist.append(image)

print('Writing hash data to ' + HASH_DATA_PATH)

with open(HASH_DATA_PATH, 'wb') as f:
    pickle.dump(hlist, f)
