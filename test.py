my_list = ["1962", "1", "3"]
my_tuple = (my_list)
for i in range(len(my_tuple)):
    print(my_tuple[i], end=" ")
print()

my_dict = {}
my_dict["1962"] = (1, 3)
for key,val in my_dict.items():
    print("{}".format(key), end=" ")
    for i in val:
        print(i, end=" ")
    print()

#mitt test sem virkar, vildi ekki stroka þitt út :D
my_dict = {}
my_dict["1962"] = (1, 3)
my_dict["the"] = (1, 2, 4, 6)
for key,val in my_dict.items():
    counter = 0
    print("{}".format(key), end=" ")
    for i in val:
        if counter != 0:
            print(end=", ")
            print(i, end="")
        else:
            print(i, end="")
            counter += 1
    print()