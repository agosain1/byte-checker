string = "100001111110001100000000001010101010001111110010010000000000000000000000000000000000000"
x = 5
len_list = []
cont = True
for i in range(0, len(string)):
    if cont:
        j = 0
        if string[i] == "0" and i+x <= len(string):
            while i+j < len(string) and string[i+j] != "1" and j < x:
                j += 1
            else:
                if j >= x:
                    print(i)
                    cont = False
        elif i+x > len(string):
            print("no result")
            cont = False
