inmutable_var = 5, " попугаев, ", 1, " обезьяна, ", True
print(inmutable_var)
print (type (inmutable_var))
print(inmutable_var [1])
print (inmutable_var [-1]) #это и предыдущее - можно
#inmutable_var[1] = "бананов, " #вот это уже нельзя, поэтому я сделаю вид, что это комментарий. Почему нельзя? Потому что это у нас кортеж, а он неизменяемый. Но мы сделаем финт ушами:
mixer= [5, "попугаев, "], 1, " обезьяна, ", True
print (mixer)
mixer [0] [1] = "бананов, "
print (mixer)
mutable_list = ["было ",10, " утят, ",1," утоп. ", False]
print (mutable_list)
print(len(mutable_list))
print (mutable_list[3])
mutable_list[4] = "улетел. "
mutable_list [5] = True
print (mutable_list)
mutable_list .append (" Туда ему и дорога!")
print (mutable_list)
print (mutable_list [-1])
print (mutable_list [3:])
print (type (mutable_list[5]))