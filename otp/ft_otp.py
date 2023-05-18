# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/18 17:00:35 by tboumadj          #+#    #+#              #
#    Updated: 2023/05/18 17:04:34 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse

if __name__ == "__main__":
# Parsing param
    parser = argparse.ArgumentParser(prog='ft_otp')
    parser.add_argument('-g')
    parser.add_argument('-k')
    args = parser.parse_args()
#Test-------------------
    print("Test...")
#----------------------------------------
