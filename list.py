mylist = []
mylist.append("one")
mylist.append("2")
mylist.append("3.0")
for x in mylist:
    print(x)


print([1,"two",3.1]*3)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 3
y_list = [y] * 3
big_list = [x_list] + [y_list]

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")