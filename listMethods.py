def main():
    values = [10,20,30,40,50,60]
    values.append(80)
    print(values)
    
    other_values = [1,2,3]
    values.extend(other_values)
    print(values)
    
    values.insert(-1,5) # gets inserted before last index(if -ve)
    print(values)
    
    print(values.index(30))
    # print(values.index(130)) # if the values is not present in list it throws valueError
    
    # if you don't want error you can use "in" operation
    
    values.remove(30) # removes the first occurrence of the value
    print(values)
    
    values.sort() # does not return anything, it only sorts
    print(values)
    
    values.reverse() # does not return anything, it only reverses
    print(values)
    
if __name__ == "__main__":
    main()