
#tuples are immutable... no accidental modifications
# faster iteration.. less memory usage 
# thread safety -- safe concurrent access (immutable)


def main():
    tup1 = (1,2,3,4,5)
    print(tup1)
    
    # tup1[0]= 10  # immutable cannot be changed
    
    val1 = [1,2,3]
    val2 = [4,5,6]
    a = 9
    
    # multiple datatypes can be stored in a tuple 
    
    tup2 = a , val1 , val2  #it is known as sequence packing
    x , y ,z = tup2  # sequence unpacking
    print(x)
    print(y)
    print(z)
    print(tup2)  # tuple can include mutable objects 
    
    
    # for single value tuple
   
    tup3 = (1,)
    print(tup3)
    
    
    #types
    
    print(type(1))
    print(type((1,)))
    print(type(()))
    print(type([]))
    print(len(tup1))
    
if __name__=="__main__":
    main()