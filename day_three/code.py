#with open("data.txt") as f_in:
#    corrupted_data= f_in.readlines(f_in)


def get_mul_str(ligne,idx) -> (int,int,bool):
    pos = ligne.find("mul(",idx)
    if pos == -1:
        return 0,pos,False
    pos2 = ligne.find(")",pos+3)
    if pos2 == -1:
        return 0, pos2, False
    next_mul = ligne.find("mul(",pos +1)
    print(pos, pos2,next_mul)
    if next_mul < pos2 and next_mul != -1:
        return 0,next_mul,True    # cas ou un mul est inséré dans un mul
    the_mul = ligne[pos:pos2+1]
    print("A traiter : ",the_mul)
    # vérifier ici que les deux éléments sont bien 2 et que ce sont des nombres
    arguments = the_mul[4:-1].split(",")
    if len(arguments)!=2:
        return 0,pos2,True
    # ici, deux valeurs
    if not (arguments[0].isnumeric() and arguments[1].isnumeric()):
        print ("pas deux numeric")
        return 0,pos2,False
    else:
        print("==> OK")
        return int(arguments[0])*int(arguments[1]), pos2,True


#with open("data.txt") as f_in:
#    corrupted_data= f_in.readlines()


st ="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
sum_mul = 0
position = 0
proceed = True
while proceed :
    val ,position ,proceed = get_mul_str(st ,position)
    sum_mul += val
    print(f"reste: {st[position:]=}")

print("Fin de traitement")
print(f"\t   {sum_mul= }")