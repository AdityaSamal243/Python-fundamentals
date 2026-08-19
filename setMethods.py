# no duplicates
# set must have immutable elements

def main():
    s1 = set()
    print(s1)
    s1.add(1)
    s1.add(2)
    print(s1)
    
   # s2 = {[1],1}
   # print(s2) # list is mutable so it cannot be added to set
   
    print(1 in s1)
    print(3 in s1)
    
    s1 = {1,2,3,4,5}
    s2 = {4,5}
    
    # to check if s1 is subset of s2
    print(s1.issubset(s2))
    print(s2.issubset(s1)) # to check if s2 is subset
    
    
    setCopy = s1.copy()
    print(setCopy)
    print(setCopy is s1)
    
    
if __name__=='__main__':
    main()