/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   spider.hpp                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/15 14:28:08 by tboumadj          #+#    #+#             */
/*   Updated: 2023/05/15 15:34:19 by tboumadj         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SPIDER_HPP
# define SPIDER_HPP
# include <curl/curl.h>
# include <curl/curlver.h>
# include <curl/easy.h>
# include <curl/mprintf.h>
# include <curl/multi.h>
# include <iostream>
# include <fstream>

class Data
{
  public:
    Data();
    ~Data();
};
#endif
