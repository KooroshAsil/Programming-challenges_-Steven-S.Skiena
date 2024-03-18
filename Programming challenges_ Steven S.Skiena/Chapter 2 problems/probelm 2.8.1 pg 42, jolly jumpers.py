def jolly_jumper(seq):
    is_there = {}
    for i in  range(1,len(seq)):
        is_there[i] = False

    for j in range(0,len(seq)-1):
        t = abs(seq[j]-seq[j+1])
        if t  in is_there.keys():
            is_there[t] = True

    if all(is_there.values()):
        print("jolly!")
        return True
    else:
        print("not jolly!")
        return False
        
def get_input():
    string = input("Enter the sequence :\nexample : 11 7 4 \n")
    seq = string.split(" ")
    seq = [int(i) for i in seq]
    return seq

seq = get_input()
print(jolly_jumper(seq))