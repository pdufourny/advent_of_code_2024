

file1 = open("file1.txt")
lst_ = file1.readlines()
file1.close

liste_1 = [element.strip()   for element in lst_]

print(liste_1)


for i in range(0,len(liste_1)-1):
    st = liste_1[i].split()
    ec = int(st[0])
    for j in range(1,len(st)):

        print(f"{ec=}  {st[j]= }  {j = }")
        if j<len(st)-1:
            if abs(ec-int(st[j]))>3 and abs(ec-int(st[j+1]))>3:
                print("ko")
                st=[]
                break
        elif abs(ec-int(st[j]))>3 :
            print("KO_1")
            st.pop(j)
            break
        else:
            ec = int(st[j])

    print(f"new_st = {st=}")
    if st == []:
        liste_1.pop(i)
print(liste_1)

