import csv, os, functions

reader= csv.reader(open("routine.csv","r",))

"""data=[]
for row in reader:
    data.append(row)


header= data.pop(0)"""

#fixed_length function used to create colums of a fixed length
def fixed_length(text,length):
    if len(str(text)) > length:
        text = text[:length]
    elif len(str(text)) < length:
        text = (text + " " * length)[:length]
    return text

def draw_table(data):
    functions.screen_clear()
    print("#" * 101)
    print("# " ,end=" ")
    for column in header:
        print(functions.fixed_length(column,20), end = "  #  ")
    print()
    print("#" * 101)

    for row in data:
        print("# " ,end=" ")
        for column in row:
            print(functions.fixed_length(column,20), end = "  #  ")
        print()
    print("#" * 101)



def which_routine():
    data=[]
    for row in reader:
        data.append(row)
    header = data.pop(0)
    return data, header

draw_table(which_routine())
