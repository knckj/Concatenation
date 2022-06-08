from itertools import permutations, chain
from collections import Counter
t1 = ["co", "dil", "ity"]
t2 = ["abc", "yyy", "def", "csv"]
t3 = ["potato", "kayak", "banana", "racecar"]
t4 = ["eva", "jqw", "tyn", "jan"]

t_all = [t1,t2,t3,t4]

expected_value_t1 = 5
expected_value_t2 = 6
expected_value_t3 = 0
expected_value_t4 = 9

expected_value_t_all = [expected_value_t1, expected_value_t2, expected_value_t3, expected_value_t4]


def solution(str_array):

    list_combinations = [list(permutations(str_array, n)) for n, str in enumerate(str_array, 1)]
    list_combinations_2 = [''.join(str_s) for perm_tuple in list_combinations for str_s in perm_tuple]

    for str_cb in list_combinations_2[:]:
        if any(list(chain(str_cb)).count(letter) > 1 for letter in str_cb):
            list_combinations_2.remove(str_cb)      
        return (0 if list_combinations_2 == [] else len(max(list_combinations_2)) )

def main():

    for index, testcases in enumerate(t_all):
        check_condition = 'OK' if solution(testcases) == expected_value_t_all[index] else 'Not good'
        print(check_condition)           
        
if __name__ == '__main__':
    main()