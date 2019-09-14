""" The different cyphers implementing Cypher as superclass """
import random
from cypher import Cypher
from crypto_utils import (
    modular_inverse, generate_random_prime,
    blocks_from_text, text_from_blocks
    )


class Caesar(Cypher):
    """ Ceasar """

    @staticmethod
    def encode(text, key):
        encoded_text = ""

        for i in text:
            encoded_text += chr((ord(i)+key) % 95)

        return encoded_text

    @staticmethod
    def decode(text, key):
        return Caesar.encode(text, 95-key)

    @staticmethod
    def generate_keys():
        return random.randint(0, 94)

    @staticmethod
    def verify(text, key):
        """ Verifies that the cypher works. """

        encoded_text = Caesar.encode(text, key)
        decoded_text = Caesar.decode(encoded_text, key)
        return decoded_text == text


class Multiplicative(Cypher):
    """ Multiplicative """

    @staticmethod
    def encode(text, key):
        encoded_text = ""

        for i in text:
            encoded_text += chr(((ord(i)-32)*key) % 95+32)

        return encoded_text

    @staticmethod
    def decode(text, key):

        inverse = modular_inverse(key, Cypher.size_alphabet)

        return Multiplicative.encode(text, inverse)

    @staticmethod
    def generate_keys():
        for i in range(random.randint(2, 94), 95):
            if modular_inverse(i, 95):
                return i

    @staticmethod
    def verify(text, key):
        """ Verifies that the cypher works. """

        encoded_text = Multiplicative.encode(text, key)
        decoded_text = Multiplicative.decode(encoded_text, key)
        return decoded_text == text


class Affine(Cypher):
    """ Affine """

    @staticmethod
    def encode(text, keys):
        encoded_multiplicative = Multiplicative.encode(text, keys[0])
        return Caesar.encode(encoded_multiplicative, keys[1])

    @staticmethod
    def decode(text, keys):
        decoded_caesar = Caesar.decode(text, keys[1])
        return Multiplicative.decode(decoded_caesar, keys[0])

    @staticmethod
    def generate_keys():
        return (
            Multiplicative.generate_keys(),
            Caesar.generate_keys()
        )

    @staticmethod
    def verify(text, key):
        """ Verifies that the cypher works. """

        encoded_text = Affine.encode(text, key)
        decoded_text = Affine.decode(encoded_text, key)
        return decoded_text == text


class Unbreakable(Cypher):
    """ Unbreakable """

    @staticmethod
    def encode(text, key):
        encoded_text = ""

        counter = 0
        for i in text:
            encoded_text += chr(((ord(i)-32) + (ord(key[counter])-32)) % 95+32)

            counter += 1
            if counter == len(key):
                counter = 0

        return encoded_text

    @staticmethod
    def decode(text, key):

        decryption_word = ""
        for i in key:
            decryption_word += chr((95-(ord(i)-32)) % 95 + 32)

        return Unbreakable.encode(text, decryption_word)

    @staticmethod
    def generate_keys():
        return

    @staticmethod
    def verify(text, key):
        """ Verifies that the cypher works. """

        encoded_text = Unbreakable.encode(text, key)
        decoded_text = Unbreakable.decode(encoded_text, key)
        return decoded_text == text


class RSA(Cypher):
    """ RSA """

    @staticmethod
    def generate_keys():

        p = 1
        q = 1
        while p == q:
            p = generate_random_prime(1024)
            q = generate_random_prime(1024)

        n = p*q
        phi = (p-1)*(q-1)

        while True:
            e = random.randint(3, phi-1)
            d = modular_inverse(e, phi)
            if d:
                break

        public_key = (n, e)
        private_key = (n, d)
        return [public_key, private_key]

    @staticmethod
    def encode(text, public_key):
        block_text = blocks_from_text(text, 256)

        for key, val in enumerate(block_text):
            block_text[key] = pow(val, public_key[1], public_key[0])

        return block_text

    @staticmethod
    def decode(block_text, private_key):

        for key, val in enumerate(block_text):
            block_text[key] = pow(val, private_key[1], private_key[0])

        return text_from_blocks(block_text, 1024)

    @staticmethod
    def verify(text, keys):

        encoded_text = RSA.encode(text, keys[0])
        decoded_text = RSA.decode(encoded_text, keys[1])
        return decoded_text == text
