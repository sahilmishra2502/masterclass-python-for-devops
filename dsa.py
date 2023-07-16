#list
#set
#tuple 
#dictionary
list_of_num =[]
print(type(list_of_num))
list_of_num.append(1)
list_of_num.append(2)
list_of_num.append("sahil")
print(list_of_num)
print(list_of_num[0])
print(list_of_num[1])
print(list_of_num[2])
#loop iteration 
for i in range(10):
    print(i)
for list in list_of_num:
    print (list)
#dictionary
dict_of_cloud = {
    "aws" :"amazon web sevices",
    "sahil": "is a good boy",
}
print(dict_of_cloud["aws"])
print(dict_of_cloud["sahil"])