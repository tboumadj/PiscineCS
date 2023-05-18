# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/18 17:00:35 by tboumadj          #+#    #+#              #
#    Updated: 2023/05/18 17:21:54 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import pyotp

def test_hotp(key):
    count = 0
    hotp = pyotp.HOTP(key)
    password = hotp.at(count)
    return (password)
#-----------------------------------

if __name__ == "__main__":
# Parsing param
    parser = argparse.ArgumentParser(prog='ft_otp')
    #parser.add_argument('-g')
    #parser.add_argument('-k')
    parser.add_argument('key', help='Key to use')
    args = parser.parse_args()
#Test-------------------
    print("Test...")
    print(args.key)
    n_pass = test_hotp(args.key)
    print("MDP_main is:", n_pass)

#----------------------------------------
