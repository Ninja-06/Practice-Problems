"""
Square Free integers are the integers which are not divisible by any square of prime number except 1.
this code will take an input on type of input passed which can be a file, other(list, tuple) along with the data
and iterates through it and computes square free integers.
"""

import numpy as np
from exception import exception
import logging

logger = logging.Logger(__name__)


class UtilsClass:

    # this class contains all the utility functions.

    def convert_file_data_to_numpy_array(self, data_file):
        data_array = np.genfromtxt(fname=data_file, delimiter=',')
        return data_array

    def convert_input_data_to_numpy_array(self, data):
        data_array = np.array(data)
        print(data_array)
        return data_array

    def get_prime_numbers(self, max_value_sqrt):
        """
          this functions takes the maximum value from array of data
          and then calculates its square_root and generates prime numbers <= square_root(max_number)
          :param max_value_sqrt: square root of max value from data list
          :return: numpy array of prime numbers
        """

        prime_num_array = np.array([])
        number_array = np.arange(2, int(max_value_sqrt), dtype=int)

        try:
            for num in np.nditer(number_array):

                # this logic for computing prime numbers is as per Fermat’s little theorem
                # reference https://en.wikipedia.org/wiki/Fermat%27s_little_theorem

                if (2 ** (num - 1)) % num == 1 or num == 2:
                    prime_num_array = np.insert(arr=prime_num_array, obj=0, values=num, axis=0)

            return prime_num_array
        except exception as e:
            logger.info(f'unable to generate prime numbers due to {e}')


class SquareFreeIntegers(UtilsClass):
    square_free_num_list = []
    non_square_free_num_list = []
    flag = False

    def __init__(self):
        pass

    def compute_square_free_numbers(self, input_type, data):
        if input_type.lower() == 'file':
            data_array = super().convert_file_data_to_numpy_array(data)
        else:
            data_array = super().convert_input_data_to_numpy_array(data)

        max_value_sqrt = np.sqrt(np.max(data_array)) + 1  # calculates square root of max value from data and adds one to it
        prime_num_array = super().get_prime_numbers(max_value_sqrt)

        # if integer is not divisible by any of square of prime integers for all the prime integers >= square root of
        # integer then it is considered as square free integer.

        try:
            for value in np.nditer(data_array):
                for num in np.nditer(prime_num_array):
                    if value % (num ** 2) == 0:
                        self.non_square_free_num_list.append(value)
                        self.flag = True
                        break
                    self.flag = False
                if not self.flag:
                    self.square_free_num_list.append(value)
        except exception as e:
            logger.info(f'unable to compute square free numbers due to {e}')

        if self.square_free_num_list:
            return self.square_free_num_list
        else:
            return "Data you provided didn't contain any square free numbers"


s1 = SquareFreeIntegers()
res = s1.compute_square_free_numbers('file', 'data.txt')
print(res)
