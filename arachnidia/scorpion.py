# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/17 15:59:18 by tboumadj          #+#    #+#              #
#    Updated: 2023/05/20 15:40:37 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
from PIL.ExifTags import TAGS
import argparse

#extrat_meta
def extract_meta(img):
    meta = img.info
    if meta is not None:
        for key, val in meta.items():
            if key == "exif":
                return
            print(f"{key}: {val}")

def extract_data(path):
    try:
        img = Image.open(path)
    except Exception as e:
        print("cannot open file...")
        return
#extract metadata
    extract_meta(img)
#extract exifdata
    exifdata = img.getexif()
    exif = {}
    for tag_id, value in exifdata.items():
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if exifdata is not None:
                print(f"{tag}: {data}")
        else:
            print("none data exif")
#-----------------------------------------------

def main():
# parsing param
    parser = argparse.ArgumentParser(prog='scoprion')
    parser.add_argument('File', help='File to extract')
    args = parser.parse_args()
#extract metoData    
    extract_data(args.File)

#--------------------------------------------------
if __name__ == "__main__":
    main()

