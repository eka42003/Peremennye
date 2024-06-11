my_dict = {"oddly":"странно", "spur":"пришпоривать","a drop at a time":"по капле за раз"}
print(my_dict)
print(my_dict["spur"])
my_dict["spur"]="стимулировать"
print(my_dict["spur"])
my_dict["afford"]= "позволить себе"
print (my_dict)
del my_dict["oddly"]
print (my_dict)
print(my_dict .get("oddly"))
my_dict .update ({"stinking":"вонючий", "fishhook": "рыболовный крючок", "searchlight":"прожектор"})
print(my_dict)
my_dict.pop("stinking")
special_1= my_dict.pop
print(special_1)
print(my_dict)

my_set={"oddly",18, True, "oddly","oddly","oddly"}
print(my_set)
my_set .update({14,15,16})
print(my_set)



