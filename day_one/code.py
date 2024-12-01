
list1 = []
liste_1_cnt = []

list2 = []
liste_2_cnt = []

file1 = open("file1.txt")
file2 = open("file2.txt")

list1 = file1.readlines()
list2 = file2.readlines()


file1.close
file2.close

liste_1 = [int(element.strip())   for element in list1]
liste_2 = [int(element.strip())   for element in list2]

#liste_1.sort()
#liste_2.sort()

similarity_score = 0

for i in liste_1:
    nb = liste_2.count(i)
    print("nbre de fois que ",i,"apparait dans la liste 2 est ",nb)
    similarity_score += nb * i



print(similarity_score)

