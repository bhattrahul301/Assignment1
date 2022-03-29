def calculte(str):

    a={"LOWER_CASE":0, "UPPER_CASE":0}
    for d in str:
        if d.isupper():
           a["UPPER_CASE"]+=1
        elif d.islower():
             a["LOWER_CASE"]+=1
    
    print("Number of Upper case characters:",a["UPPER_CASE"])
    print("Number of Lower case Characters:",a["LOWER_CASE"])

calculte('The quick Brow Fox')



