# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/17 15:59:18 by tboumadj          #+#    #+#              #
#    Updated: 2023/05/22 14:12:41 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
import piexif
import argparse

#extrat_meta
def extract_meta(path):
    try:
        img = Image.open(path)
    except Exception as e:
        print("cannot open file...")
        return
    meta = img.info
    if meta is not None:
        for key, val in meta.items():
            if key == "exif":
                return
            print(f"{key}: {val}")
    img.close()
#----------------------------------------------

def extract_exif(exif_data):
    try:
        for ifd_name in exif_data:
            print(f"IFD: {ifd_name}")
            for tag in exif_data[ifd_name]:
                try:
                    tag_name = piexif.TAGS[ifd_name][tag]["name"]
                except Exception as e:
                    return
                tag_value = exif_data[ifd_name][tag]
                print(f"{tag_name}: {tag_value}")
    except Exception as e:
        return
#----------------------------------------------------

def get_exif_data(path):
    exif_info = piexif.load(path)
    return exif_info
#-----------------------------------------------

def main():
# parsing param
    parser = argparse.ArgumentParser(prog='scoprion')
    parser.add_argument('File', help='File to extract')
    args = parser.parse_args()
#extract Data
    extract_meta(args.File)
    exif_data = get_exif_data(args.File)
    extract_exif(exif_data)
#--------------------------------------------------
if __name__ == "__main__":
    main()

