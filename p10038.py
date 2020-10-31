# import sys

# sys.stdin = open("input.txt")
# sys.stdout = open("output.txt", 'w')

def isJumper(arr):
    jump = {}

    for i in range(1, len(arr)):
        jump[i] = 0

    for i in range(len(arr)-1):
        sub = abs(arr[i]-arr[i+1])
        if(sub<=len(arr)-1):
            jump[sub] = 1

    # print(jump)

    for i in jump:
        if(jump[i] == 0):
            return 0

    return 1 


try:
    while(1):
        arr = input().strip()
        arr = arr.split(" ")
        arr = [int(x) for x in arr[1:]]

        if(isJumper(arr) == 1):
            print("Jolly")
        else:
            print("Not jolly")

except EOFError:
    pass






