from itertools import permutations

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

    list_combinations = list()
    for n in range(len(str_array) + 1):
        list_combinations += list(permutations(str_array, n))

    list_combinations_2 = list()

    for comb_tuple in list_combinations:
        str_comb = ''
        i = 0
        for i in range(len(comb_tuple)):
            str_pap = comb_tuple[i]
            str_comb += str_pap
            i += 1
        list_combinations_2.append(str_comb)
  

    for str_cb in list_combinations_2[:]:
        str_cb_splitted = [x for x in str_cb]
        for letter in str_cb_splitted:
            check_value = str_cb.count(letter)
            if check_value > 1:
                list_combinations_2.remove(str_cb)
                break

    return len(max(list_combinations_2))

def main():

    i = 0
    for testcases in t_all:
        if solution(testcases) == expected_value_t_all[i]:
            print("test passed")
        else:
            print('coś zjebałem')
        i += 1       
        
if __name__ == '__main__':
    main()