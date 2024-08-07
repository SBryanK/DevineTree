# -*- coding: utf-8 -*-
"""OPTICAL CHARACTER RECOGNITION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14gBqApRphl8gfdFqEr-ZsspDlxkVmspC
"""

import pandas as pd
import numpy as np

from glob import glob
from tqdm.notebook import tqdm

import matplotlib.pyplot as plt
from PIL import Image

plt.style.use('ggplot')

# We are goin to extract text from image using 3 OCR (Optical Character Recognition) Library

annot = pd.read_parquet('annot.parquet')
imgs = pd.read_parquet('img.parquet')
img_fns = glob('train_images/*')

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(plt.imread(img_fns[0]))
ax.axis('off')
plt.show()

# Define how to extract image id and file name
# And use the ID to annotate the correct ID in the dataframe
image_id = img_fns[0].split('/')[-1].split('.')[0]
annot.query('image_id == @image_id')

fig, axs = plt.subplots(5, 5, figsize=(20, 20))
axs = axs.flatten()
for i in range(25):
    axs[i].imshow(plt.imread(img_fns[i]))
    axs[i].axis('off')
    image_id = img_fns[i].split('/')[-1].rstrip('.jpg')
    n_annot = len(annot.query('image_id == @image_id'))
    axs[i].set_title(f'{image_id} - {n_annot}')
plt.show()

#PYTESSERACT

import pytesseract
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(plt.imread(img_fns[11]))
ax.axis('off')
plt.show()

# EASYOCR

import easyocr

reader = easyocr.Reader(['en'], gpu = True)
results = reader.readtext(img_fns[11])
pd.DataFrame(results, columns=['bbox','text','conf'])

# KERAS_OCR

import keras_ocr
from keras_ocr.pipeline import pipeline
pipeline = pipeline()
results = pipeline.recognize([img_fns[11]])
pd.DataFrame(results[0], columns=['text', 'bbox'])

fig, ax = plt.subplots(figsize=(10, 10))
keras_ocr.tools.drawAnnotations(plt.imread(img_fns[11]), results[0], ax=ax)
ax.set_title('Keras OCR Result Example')
plt.show()

#PLOT RESULT: EASYOCR and KERAS_OCR

def plot_compare(img_fn, easyocr_df, kerasocr_df):
    img_id = img_fn.split('/')[-1].split('.')[0]
    fig, axs = plt.subplots(1, 2, figsize=(15, 10))

    easy_results = easyocr_df.query('img_id == @img_id')[['text','bbox']].values.tolist()
    easy_results = [(x[0], np.array(x[1])) for x in easy_results]
    keras_ocr.tools.drawAnnotations(plt.imread(img_fn),
                                    easy_results, ax=axs[0])
    axs[0].set_title('easyocr results', fontsize=24)

    keras_results = kerasocr_df.query('img_id == @img_id')[['text','bbox']].values.tolist()
    keras_results = [(x[0], np.array(x[1])) for x in keras_results]
    keras_ocr.tools.drawAnnotations(plt.imread(img_fn),
                                    keras_results, ax=axs[1])
    axs[1].set_title('keras_ocr results', fontsize=24)
    plt.show()