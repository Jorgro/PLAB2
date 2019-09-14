"""
Cypher-superclass
"""
import abc


class Cypher:
    """
    Cypher-superclass
    """

    __metaclass__ = abc.ABCMeta

    size_alphabet = 95

    @staticmethod
    @abc.abstractmethod
    def encode(text, key):
        """ Encode abstract static """
        return

    @staticmethod
    @abc.abstractmethod
    def decode(text, key):
        """ Decode abstract static """
        return

    @staticmethod
    @abc.abstractmethod
    def generate_keys():
        """ Generate_keys abstract static """
        return

    @staticmethod
    @abc.abstractmethod
    def verify(text, key):
        """ Verifies that the cypher works. """
        return
