# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/18 17:00:35 by tboumadj          #+#    #+#              #
#    Updated: 2023/05/19 14:02:28 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import pyotp
import os

def extract_file(path_file):
    file = open(path_file, "r")
    inside = file.read()
    file.close()
    return (inside)

#----------------------------------

def creat_out(key):
    file = open("ft_otp.key", "w")
    file.write(key)
    file.close()
    print("key create in ft_otp.key ..")

#-----------------------------------

def dir_hotp(str, _k):
    count = 0
    hotp = pyotp.HOTP(str)
    password = hotp.at(count)
    #create folder with key
    if _k == True:
        creat_out(password)
    #---
    return (password)

#-----------------------------------

def main():
# Parsing param
    parser = argparse.ArgumentParser(prog='ft_otp')
    parser.add_argument('-g', '--hex')
    parser.add_argument('-k', '--temp')
    args = parser.parse_args()
#main-------------------
    if args.hex:
        _k = True
        _dt = extract_file(args.hex)
        n_key = dir_hotp(_dt, _k)
    elif args.temp:
        _k = False
        _dt = extract_file(args.temp)
        n_key = dir_hotp(_dt, _k)
    print("key_main is:", n_key)

#----------------------------------------
if __name__ == "__main__":
    main()
