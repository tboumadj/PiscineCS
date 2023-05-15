# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj@student.42mulhouse.fr <tboumadj>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/09 19:11:05 by tboumadj@student  #+#    #+#              #
#    Updated: 2023/05/15 16:31:27 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#FLAG

NAME		=		Spider
CC			=		c++
FLAGS		=		-Wall -Wextra -Werror -std=c++98
RM			=		rm -f
CHECK		=		-fsanitize=address
##LDFLAGS=		-L/Users/tboumadj/.brew/opt/curl/lib
##CPPFLAGS=		-I/Users/tboumadj/.brew/opt/curl/include
##PKG_CONFIG_PATH = /Users/tboumadj/.brew/opt/curl/lib/pkgconfig

#PATH

SRCS		=		src/main.cpp
OBJS		=		$(SRCS:.cpp=.o)
HEADER	=		inc/spider.hpp

#COLORS

_GREY		=		$'\x1b[33m
_GREEN	=		$'\x1b[32m

##

.o : .c $(HEADER) Makefile
								@$(CC) $(FLAGS) -lcurl -c $< -o $(<:cpp=o) $@

$(NAME):	$(OBJS)
									@echo "$(_GREY)Compilation de Spider en cours...$(_END)"
									$(CC) $(OBJS) $(FLAGS) -lcurl -o $(NAME) #(CHECK)
									@echo "$(_GREEN)$(_BOLD)Fin de la compilation!$(_END)"

.SILENT	: $(OBJS) $(NAME)

all	:		$(NAME)

clean	:
				@$(RM) $(OBJS)

fclean	:	clean
					@$(RM) $(NAME)
					@echo "$(_GREEN)$(_BOLD)Exec & .o have been erased!$(_END)"
re	:	 fclean all

.PHONY	:	all clean fclean re
