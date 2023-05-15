# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Spyder.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/15 17:41:06 by tboumadj          #+#    #+#              #
#    Updated: 2023/05/15 20:39:15 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import urllib.request
import requests
import argparse
import os
from lxml import html
import lxml.html
import lxml.etree

def extract_img(arg):
    print("URL =", arg)
    response = requests.get(arg)
    html_doc = response.content
    tree = html.fromstring(html_doc)
    img_tags = tree.xpath("//img/@src")
    ##TEST---------
    for tag in img_tags:
        download_img(tag)

def download_img(addr):
# creation du fichier data
    print("img:", addr)
    drt = "data"
    if not os.path.exists(drt):
        os.mkdir(drt)
    url = addr
    filename = os.path.basename(addr)
    filename = filename[-21:]
# Télécharger l'image
    way_file = os.path.join(drt, filename)
    try:
        urllib.request.urlretrieve(url, way_file)
        print(" Img download success!")
    except urllib.error.HTTPError as e:
        print("error with download..", e.code, e.reason)
        return
    except urllib.error.URLError as e:
        print("error with download..", e.reason)
        return
    except Exception as e:
        print("failed..")
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Spider')
    parser.add_argument('URL', help='URL to spider')
    args = parser.parse_args()
    #print("l url est:", args.URL)
    extract_img(args.URL)
    #download_img(args.URL)



