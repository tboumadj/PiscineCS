/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/15 14:27:01 by tboumadj          #+#    #+#             */
/*   Updated: 2023/05/15 16:38:46 by tboumadj         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../inc/spider.hpp"

/*int main(int argc, char **argv)
{
  CURL *curl = curl_easy_init();
  if (!curl)
  {
    std::cerr << "Error: cant init libcurl" << std::endl;
    return (-1);
  }
  curl_easy_setopt(curl, CURLOPT_URL, argv[1]);

  std::ofstream outfile(argv[2], std::ios::binary);
  if (!outfile)
  {
    std::cerr << "Error: cant create outfile" << std::endl;
    curl_easy_cleanup(curl);
    return (-1);
  }

  curl_easy_setopt(curl, CURLOPT_WRITEDATA, &outfile);

  CURLcode res = curl_easy_perform(curl);
  if(res != CURLE_OK)
  {
    std::cerr << "ErrorL: " << curl_easy_strerror(res) << std::endl;
    outfile.close();
    curl_easy_cleanup(curl);
    return (-1);
  }
  outfile.close();
  curl_easy_cleanup(curl);
  
  std::cout << "Image download successfully" << std::endl;
  return (0);
}*/


#include <curl/curl.h>
#include <iostream>
#include <fstream>

int main()
{
    // initialiser curl
    curl_global_init(CURL_GLOBAL_ALL);

    // créer une instance de curl
    CURL *curl = curl_easy_init();

    if(curl) {
        // définir l'URL de téléchargement
        curl_easy_setopt(curl, CURLOPT_URL, "https://example.com/image.png");

        // créer un fichier pour stocker l'image
        std::ofstream image_file("image.png", std::ios::binary);

        // définir la fonction de rappel pour écrire les données de l'image dans le fichier
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, [](void *ptr, size_t size, size_t nmemb, void *userdata) -> size_t {
            std::ostream *stream = reinterpret_cast<std::ostream*>(userdata);
            stream->write(reinterpret_cast<const char*>(ptr), size * nmemb);
            return size * nmemb;
        });

        // définir le flux pour écrire les données de l'image dans le fichier
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &image_file);

        // exécuter la requête de téléchargement
        CURLcode res = curl_easy_perform(curl);

        // vérifier si le téléchargement a réussi
        if(res != CURLE_OK) {
            std::cerr << "Erreur lors du téléchargement : " << curl_easy_strerror(res) << std::endl;
        }

        // libérer les ressources
        curl_easy_cleanup(curl);
    }

    // arrêter curl
    curl_global_cleanup();

    return 0;
}
