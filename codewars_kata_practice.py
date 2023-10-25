def count_sheeps(sheep):
  present = [present for present in sheep if present == True]
  return sum(present)


array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ];

print(array1)