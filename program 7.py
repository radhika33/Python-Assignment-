# ques 7:program to display which letter are in the two string but not in both.

from collections import Counter
list1 = [1,2,3,4,5,6,9,7,11]
list2 = [7,8,3,4,1,45,65,11]
dict1 = Counter(list1)
dict2 = Counter(list2)
dictcommon = dict1&dict2
commonlist = list(dictcommon.elements())
print("The common element in the two list",commonlist)
for i in commonlist:
    list1.remove(i)
    list2.remove(i)
print("First list after the removal of the common string",list1)
print("Second list after the removal of the common string",list2)
