itemitcart = 0

if itemitcart != 2:
    pass

assert(itemitcart == 0)


#try , catch

try:
    with open('fileor.txt', 'r') as reader:
        reader.read()

except:
    print("some who")



try:
    with open('fileor.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)