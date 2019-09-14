import abc
import multiprocessing
import queue
from cyphers import Caesar, Multiplicative, Unbreakable
from crypto_utils import modular_inverse


class Person:
    """
    Person-superklasse for Hacker, Receiver og Sender.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, cipher):
        self.cipher = cipher
        self.key = ""

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    @abc.abstractmethod
    def operate_cipher(self, text):
        return


class Sender(Person):

    def operate_cipher(self, text):
        return self.cipher.encode(text, self.key)


class Receiver(Person):

    def operate_cipher(self, text):
        return self.cipher.decode(text, self.key)


def read_dictionary(filepath):
    word_list = []
    with open(filepath, 'r') as file:
        for i in file:
            word_list.append(i.strip())

    return word_list


class Hacker():

    WORD_LIST = read_dictionary('Project3/english_words.txt')

    """ def __init__(self):
        self.skip_jobs = False """

    def operate_cipher(self, text):

        processes = [
            self.hack_caesar, self.hack_multiplicative,
            self.hack_affine, self.hack_unbreakable
        ]

        jobs = []
        q = multiprocessing.Queue()

        for i in range(4):
            process = multiprocessing.Process(
                target=processes[i],
                args=(text, q))
            jobs.append(process)

            process.start()
        data = []

        main_processing = True
        while main_processing:

            try:
                msg = q.get()
                data.append(msg)
                print(data)
                if msg[3]:

                    for proc in jobs:
                        proc.terminate()
                        proc.join()

                    main_processing = False
                else:
                    if len(data) == 4:
                        main_processing = False
                        for proc in jobs:
                            proc.terminate()
                            proc.join()

            except queue.Empty as e:
                continue

        data = max(data, key=lambda item: item[1])
        best_sentence = data[0]
        max_probability = data[1]
        index = data[2]

        methods = ['Caesar', 'Multiplicative', 'Affine', 'Unbreakable']

        return (f'{methods[index]}: "{best_sentence}"'
                f' with {max_probability} probability.')

    @staticmethod
    def test_combination(test):
        probability = 0
        text = test.split(' ')
        for i in text:
            if i.lower() in Hacker.WORD_LIST:
                probability += 1/len(text)
        return probability

    @staticmethod
    def find_best_combination(sentences_and_probabilities, number, boolean):
        max_probability = sentences_and_probabilities[0][1]
        best_sentence = sentences_and_probabilities[0][0]

        for i in sentences_and_probabilities:
            if i[1] > max_probability:
                max_probability = i[1]
                best_sentence = i[0]

        return (best_sentence, max_probability, number, boolean)

    def hack_caesar(self, text, queue):
        sentences_and_probabilities = []

        for i in range(95):
            sentence = Caesar.encode(text, i)
            probability = Hacker.test_combination(sentence)

            if probability == 1:
                queue.put((sentence, probability, 0, True))
                return

            sentences_and_probabilities.append((sentence, probability))
        # Print(sentences_and_probabilities)
        queue.put(
            Hacker.find_best_combination(sentences_and_probabilities, 0, False)
            )

    @staticmethod
    def possible_numbers():

        possible_numbers = []
        for i in range(95):
            if modular_inverse(i, 95):
                possible_numbers.append(i)

        return possible_numbers

    def hack_multiplicative(self, text, queue):
        sentences_and_probabilities = []

        possible_numbers = Hacker.possible_numbers()

        for i in possible_numbers:

            sentence = Multiplicative.encode(text, i)
            probability = Hacker.test_combination(sentence)

            if probability == 1:
                
                queue.put((sentence, probability, 1, True))
                return

            sentences_and_probabilities.append((sentence, probability))
        # Print(sentences_and_probabilities)
        queue.put(
            Hacker.find_best_combination(sentences_and_probabilities, 1, False)
            )

    def hack_affine(self, text, queue):

        sentences_and_probabilities = []
        possible_numbers = Hacker.possible_numbers()

        for i in range(95):
            for j in possible_numbers:

                caesar_decryption = Caesar.decode(text, i)
                sentence = Multiplicative.decode(caesar_decryption, j)
                probability = Hacker.test_combination(sentence)

                if probability == 1:
                    
                    queue.put((sentence, probability, 2, True))
                    return

                sentences_and_probabilities.append((sentence, probability))

        queue.put(
            Hacker.find_best_combination(sentences_and_probabilities, 2, False)
            )

    def hack_unbreakable(self, text, queue):
        sentences_and_probabilities = []

        for i in Hacker.WORD_LIST:

            sentence = Unbreakable.decode(text, i.upper())
            probability = Hacker.test_combination(sentence)

            if probability == 1:
                queue.put((sentence, probability, 3, True))
                return

        sentences_and_probabilities.append((sentence, probability))
        queue.put(
            Hacker.find_best_combination(
                sentences_and_probabilities,
                3,
                False
            ))
