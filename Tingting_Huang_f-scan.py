import sys
import copy

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
    left=right=-1
    #print(remaining)
    for index in range(len(remaining)):
        if remaining[index]<= start:
            left = index
        if remaining[index]> start:
            right = index
            break

def scheduler(q1,q2):
    i=0
    while(1):
        while (len(q2) < 10 and len(line2) != 0):
            #print (i)
            # print (line2)
            
            q2.append(int(line2[0]))
            del line2[0]
    
    
    
        q1=copy.deepcopy(q2)
        
        q2=[]
        q1.sort()
        #print(q1)
        #print (last)
        scan(last,q1)
        
        if(len(line2) == 0 and q2==[]):
            break






def scan(current, remaining):
    findPosition(current, remaining)
    global last, left, right, res, sum
    #print(left,right)
    #print(remaining)
    if ((current - remaining[left]) <= (remaining[right] - current) and right!=-1 and left!=-1 ):
        i=left
        while(i>=0):
            
            res.append(remaining[i])
            i=i-1
        i = left+1
        while(i<len(remaining)):
            
            res.append(remaining[i])
            i=i+1
        #print(remaining[i])
        last = remaining[-1]
        sum+=current-0+remaining[-1]
    
    elif((current - remaining[left]) > (remaining[right] - current) and right!=-1 and left!=-1 ):
        i=right
        while (i < len(remaining)):
            
            res.append(remaining[i])
            i = i + 1
        i=right-1
        while (i >= 0):
            
            res.append(remaining[i])
            i = i - 1
        
        last = remaining[0]
        sum+=199*2 - current - remaining[0]
    
    
    elif(left==-1 and right!=-1):
        for index in range(0,len(remaining)):
            res.append(remaining[index])
        last = remaining[-1]
        sum+=remaining[-1]-current
    elif(right==-1 and left!=-1):
        for index in range(len(remaining)-1 , -1, -1):
            res.append(remaining[index])
        last = remaining[0]
        sum+=current - remaining[0]
    elif(left==-1 and right==-1):
        res.append(remaining[0])
        last = remaining[0]
        sum+=abs(current-remaining[0])

try:
    current = int(line1)
    remaining = []
    for nums in line2:
        remaining.append(int(nums))
    remaining.sort()
    last = current
    q1=[]
    q2=[]
    scheduler(q1,q2)

    for nums in range(len(res)-1):
        print res[nums],",",
    print res[-1]
    print sum
    print last,sum

except ValueError:
    print "Invalid Input! Please try again."
