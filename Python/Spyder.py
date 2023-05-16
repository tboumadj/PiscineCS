# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Spyder.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/15 17:41:06 by tboumadj          #+#    #+#              #
#    Updated: 2023/05/16 14:31:25 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import urllib.request
from urllib.parse import urljoin
import requests
import argparse
import os
from lxml import html
import lxml.html
import lxml.etree

#Fonction extraction des images dans les balise + check URL
def extract_img(arg, folder):
#Test response et extract des balise
    print("URL =", arg)
    try:
        response = requests.get(arg)
    except Exception as e:
        print ("URL invalid.. or no response..")
        #print (e)
        return
    html_doc = response.content
    tree = html.fromstring(html_doc)
# extract des balise src dans img
    img_tags = tree.xpath("//img/@src")
    ##TEST---------
    for tag in img_tags:
        download_img(tag, folder)
#-----------------------------------------------

#Fonction telechargement des image + check des extensions
def download_img(addr, folder):
# creation du fichier data
    drt = folder
    if not os.path.exists(drt):
        os.mkdir(drt)
# creation et check du name de l 'image et son extension
    url = addr
    if (url.startswith("//")):
        url = "https:" + url
    print("img:", url)
    filename = os.path.basename(addr)
    #filename = filename[-21:]
    check_ext = filename.split(".")[-1]
    valid_ext = ('jpg', 'jpeg', 'png', 'gif', 'bmp')
    if check_ext not in valid_ext:
        print("not valid extensions..")
        return
# Télécharger l'image
    way_file = os.path.join(drt, filename)
    try:
        urllib.request.urlretrieve(url, way_file)
        print("Img download with success!")
    except urllib.error.HTTPError as e:
        print("error with download..", e.code, e.reason)
        return
    except urllib.error.URLError as e:
        print("error with download..", e.reason)
        return
    except Exception as e:
        print("failed..")
        return
#--------------------------------------------

#Fonction controle de profondeur #Test
def depth_level(url, depth):
    if depth > max_depth:
        return
    visited.add(url)
    try:
        response = requests.get(url)
    except:
        return
    tree = html.fromstring(response.content)
    links = tree.xpath("//a/@href")
    for link in links:
        if link.startswith("/") or link.startswith(url):
            href = urljoin(url, link)
            if href not in visited:
                depth_level(href, depth+1)
    return
#-------------------------------------------

if __name__ == "__main__":
# parsing des param
    parser = argparse.ArgumentParser(prog='Spider')
    parser.add_argument('URL', help='URL to spider')
    parser.add_argument('-p', '--path', type=str, default='data', help='Folder to stock')
    args = parser.parse_args()
# envoi dans le programme d extract
    #extract_img(args.URL, args.path)
# TEST-------
    max_depth = 10
    depth = 0
    visited = set()
    depth_level(args.URL, depth)
    print("Maximum depth of the website:", max([len(x.split("/"))-3 for x in visited]))

#-------------------------------------------


