"""
This file gets all urls from a .txt file and downloads each image on that url.
This was used to download all images the CNN was trained and tested on.
"""

from imutils import paths
import argparse
import requests
import cv2
import os


# Get all urls and define where the images should be saved
category = "burgers"
urls = os.path.join("/Users/pabloblanco/Desktop", "urls.txt")
output = os.path.join("/Users/pabloblanco/Desktop/Places/ml/datasets", category)


# Grab the list of urls from the input file and convert them to list
# Then initialize the total number of images downloaded so far
rows = open(urls).read().strip().split("\n")
total = 0
print(f"Number of rows: {len(rows)}")


# Cut down the urls list if it passes the arbitrary limit of 500
# This was done to ensure having balanced datasets and make the training process simpler
if len(rows) > 500:
    rows = rows[:500]
    
# Iterate over each url to download the image
for url in rows:
	try:
		# try to download the image
		r = requests.get(url, timeout=60)

		# save the image to disk
		p = os.path.join(output, f"{str(total).zfill(8)}.jpg")
		f = open(p, "wb")
		f.write(r.content)
		f.close()

		# update the counter
		print(f"[INFO] downloaded: {p}")
		total += 1

	# handle if any exceptions are thrown during the download process
	except:
		print(f"[INFO] error downloading {p}...skipping")

