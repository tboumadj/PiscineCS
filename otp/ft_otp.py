# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/18 17:00:35 by tboumadj          #+#    #+#              #
#    Updated: 2023/05/18 18:05:11 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import pyotp
import os

def test_hotp(key):
    count = 0
    hotp = pyotp.HOTP(key)
    password = hotp.at(count)
    return (password)
#-----------------------------------

def dir_hotp(str, key):
    count = 0
    hotp = pyotp.HOTP(key)
    password = hotp.at(count)
    #create folder with key
    file = open("ft_otp.key", "w")
    file.write(password)
    file.close()
    print("key create in ft_otp.key ..")
    return (password)
#-----------------------------------

if __name__ == "__main__":
# Parsing param
    parser = argparse.ArgumentParser(prog='ft_otp')
    parser.add_argument('-g', '--hex')
    #parser.add_argument('-k')
    parser.add_argument('key', help='Key to use')
    args = parser.parse_args()
#Test-------------------
    print("Test...")
    print(args.key)
    if args.hex:
        n_pass = dir_hotp(args.hex, args.key)
    else:
        n_pass = test_hotp(args.key)
    print("MDP_main is:", n_pass)

#----------------------------------------
