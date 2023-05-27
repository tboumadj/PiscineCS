# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tboumadj <tboumadj@student.42mulhouse.fr>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/24 15:04:43 by tboumadj          #+#    #+#              #
#    Updated: 2023/05/24 15:27:58 by tboumadj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii

def decrypt_aes(key, ciphertext, iv):
    # Vérifier que la clé a une longueur valide (128, 192 ou 256 bits)
    valid_key_lengths = [16, 24, 32]
    key_length = len(key)
    if key_length not in valid_key_lengths:
        raise ValueError("La clé doit avoir une longueur de 128, 192 ou 256 bits.")

    # Convertir la clé, le texte chiffré et le vecteur d'initialisation (IV) en bytes
    key_bytes = binascii.unhexlify(key)
    ciphertext_bytes = binascii.unhexlify(ciphertext)
    iv_bytes = binascii.unhexlify(iv)

    # Créer un objet Cipher avec l'algorithme AES, le mode de chiffrement CBC et le backend par défaut
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv_bytes), backend=default_backend())

    # Créer un objet decrypteur
    decryptor = cipher.decryptor()

    # Déchiffrer le texte chiffré
    decrypted = decryptor.update(ciphertext_bytes) + decryptor.finalize()

    # Retourner le texte déchiffré sous forme hexadécimale
    return binascii.hexlify(decrypted).decode()

# Clé de chiffrement (doit avoir une longueur de 128, 192 ou 256 bits)
key = '0123456789ABCDEF0123456789ABCDEF'

# Chaîne hexadécimale de 64 caractères chiffrée
ciphertext = '9C6B242B56C4B7C980A0426ABFF54F1FD11B45FCD444B90629F17C40C86DC2F3'

# Vecteur d'initialisation (IV) correspondant à la chiffrée
iv = 'A0B0C0D0E0F0A1B2C3D4E5F6A7B8C9D0'

# Appel de la fonction de déchiffrement AES
decrypted_text = decrypt_aes(key, ciphertext, iv)

print("Texte déchiffré :", decrypted_text)
