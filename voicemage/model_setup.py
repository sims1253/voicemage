import site
import os
from distutils.dir_util import copy_tree


site_path = site.getsitepackages()[0] + "/speech_recognition/pocketsphinx-data/de-DE"

if not os.path.exists(site_path):
    copy_tree("../models/de-DE", site_path)
else:
    print("It appears that the german model is already installed.")
