from function import *
#initialize the file path
item_path = 'Item.txt'
transaction_path = 'Transaction.txt'

MIN_SUPPORT = 2
MAX_DATASET_SIZE = 4

#get the item array
item_array = read_lines(item_path)
item_array = dataProcess(item_array)
print("Items are listed below:")
print(item_array)
#get the transaction array
transaction_array = read_lines(transaction_path)
transaction_array = dataProcess(transaction_array)
print("Transaction records are listed below:")
print(transaction_array)

candidate_array = item_array
for i in range(0,MAX_DATASET_SIZE):
    #count the condidate frequency
    candi_dic = count_in_Transac(candidate_array,transaction_array)
    print('The candidate for the {} items dataset has {} components:'.format(i + 1, len(candidate_array)))
    for k,value in enumerate(candidate_array):
        print("Data:{}  Frequency:{}".format(candidate_array[k],candi_dic[k]))
    #select condidate whose frequency bigger than MIN_SUPPORT
    result = choose_res_from_candi(candidate_array,candi_dic,MIN_SUPPORT)
    candi_dic = count_in_Transac(result,transaction_array)
    print('After selected,the {} items dataset has {} components:'.format(i+1,len(result)))
    for j,value in enumerate(result):
        print("Data:{}  Frequency:{}".format(result[j],candi_dic[j]))
    #generate new candidate
    candidate_array = generate_candidate(result)




