def main():
    print(bool(0))
    print(bool(1)) 
    # 0 and empty values are considered False,
    # empty stings,list,tupple,dict,sets are false
    
    print(bool(()))
    print(bool([1]))
    print(bool(None))
    print(1<10)
    print(1<2<3)
    
if __name__=="__main__":
    main()