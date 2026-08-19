def main():
    li = [1,2,3]
    print(li[0],end=" ")
    print(li[1],end=" ")
    print(li[2])
    
    li2 = li  #li2 doesn't create a copy instead li2 points to li (same mem)
    print(li2)
    
    # list functions
    values = [1,4,9,16]
    sum = 0
    for num in values:
        sum += num
    print(sum)
    
    # in = it is used to check if an element appears in the list or other collection.
    if 1 in values:
        print('yohoo')
        
    #Range in python
    
    for i in range(4):   # iterates from 0 to n-1 i.e 3
        print(i)
        
    for i in range(12,15):  # iterates from a to b-1
        print(i)
    
if __name__=="__main__":
    main()