import os
import copy

#read data from the txt file
def read_lines(file_path):
    if os.path.exists(file_path):
        array = []
        with open(file_path, 'r') as lines:
            for line in lines:
                line = line.strip('\n')
                line = line.strip('\r')
                array.append(line)
        return array
    else:
        print('file not exist: ' + file_path)
        return None
#to get the data form we want
def dataProcess(dataArray):
    final_Array = []
    for line in dataArray:
        temp_Array = line.split(' ')
        final_Array .append(temp_Array)
    return final_Array

def generate_candidate(input_array):
    length_array = len(input_array)
	#to make the program robust,if the input_array is blank,we return the double [[]]
    if(length_array==0):
        return [[]]
	#to get the length of input frequency items' each item 
    length_item = len(input_array[0])
	#initialize the final result we want 
    final_array = []
	
	#to compare whether two list have (length_item - 1) items in common
	#if they do have,we can generate a new candidate
    for i in range(0, length_array):
        for k in range(i + 1, length_array):
            if (input_array[i][0:length_item - 1] == input_array[k][0:length_item - 1]):
                temp_array = copy.deepcopy(input_array[i][0:length_item - 1])
                temp_array.append(input_array[i][length_item - 1])
                temp_array.append(input_array[k][length_item - 1])
				#to find whether the candidate in the transaction records
				#if not,delete the candidate
                if (is_candidate(temp_array, input_array)):
                    final_array.append(temp_array)
    return final_array

#delete some candidate from the k-1 frequent itemset
#the standard is whether the candidate is in the transaction records
def is_candidate(candidate,input_array):
    length = len(candidate)
    for i in range(0,length):
        temp_array = copy.deepcopy(candidate)
        temp_array.remove(candidate[i])
        if(temp_array not in input_array):
            return False
    return True

def count_in_Transac(candidate_array,Transaction):
    len_candi = len(candidate_array)
    len_transac = len(Transaction)
    final_dic = {}


    for i in range(0,len_candi):
        count_num = 0
        for k in range(0,len_transac):
            if(array_belong(candidate_array[i],Transaction[k])):
                count_num = count_num + 1
        final_dic[i] = count_num

    return final_dic


#find whether array1 belongs to array2
def array_belong(array1,array2):
    len_1 = len(array1)

    for i in range(0,len_1):
        if(array1[i] not in array2):
            return False
    return True


def choose_res_from_candi(candidate_array,candidate_dic,mim_sup):
    final_res = []

    for i,value in enumerate(candidate_array):
        if(candidate_dic[i]>=mim_sup):
            final_res.append(value)
    return final_res
