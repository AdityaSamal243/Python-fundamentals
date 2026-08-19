def main():
    a = [1,2,3]
    b = [1,2,3]
    print(b is a)
    c = a  #it means c points to same location as a.
    print(c is a)
    print(len("Aditya Tanu"))
    
if __name__=="__main__":
    main()