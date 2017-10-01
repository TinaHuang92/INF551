import sys


sum=0
res=[]


try:
    f=open(sys.argv[1],"r")
    line1 = (f.readline())
    line2 =  (f.readline()).split(",")

finally:
    if f:
        f.close()



def findPosition(start, remaining):
    global left, right
    left = right = -1
    for index in range(len(remaining)):
        if remaining[index] <= start:
            left = index
        if remaining[index] > start:
            right = index
            break


def sstf(current, remaining):
    findPosition(current, remaining)
    global last, left, right, res, sum
    if ((current - remaining[left]) <= (remaining[right] - current) and right != -1 and left != -1):
        i = left
        while (i >= 0):
            res.append(remaining[i])
            i = i - 1
        i = left + 1
        while (i < len(remaining)):
            res.append(remaining[i])
            i = i + 1
        last = remaining[-1]
        sum += current - remaining[0] + remaining[-1]-remaining[0]

    elif ((current - remaining[left]) > (remaining[right] - current) and right != -1 and left != -1):
        i = right
        while (i < len(remaining)):
            res.append(remaining[i])
            i = i + 1
        i = right - 1
        while (i >= 0):
            res.append(remaining[i])
            i = i - 1
        
        last = remaining[0]
        sum += remaining[-1] * 2 - current - remaining[0]


    elif (left == -1 and right != -1):
        for index in range(0, len(remaining)):
            res.append(remaining[index])
        last = remaining[-1]
        sum += remaining[-1] - current
    elif (right == -1 and left != -1):
        for index in range(len(remaining) - 1, -1, -1):
            res.append(remaining[index])
        last = remaining[0]
        sum += current - remaining[0]
    elif (left == -1 and right == -1):
        res.append(remaining[0])
        last = remaining[0]
        sum += abs(current - remaining[0])




try:
    current = int(line1)
    remaining = []
    for nums in line2:
        remaining.append(int(nums))
    remaining.sort()
    last = current

    sstf(current,remaining)
    for nums in range(len(res)-1):
        print res[nums],",",
    print res[-1]
    print sum
    print last,",",sum

except ValueError:
    print("Invalid Input! Please try again.")
