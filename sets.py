# set supports == union,intersection,difference,symmetry
# set() function used to create set 

def main():
    basket = {'apple','orange','apple','mango','pear','pear','grapes'}
    print(basket)  # duplicates are removed
    
    a = set('hahahahhab')
    b = set('klklkllb')
    print(b)
    print(a)
    print(a-b)
    print(a|b)
    print(a&b)
    print(a^b)  # in a or b but not both
    
    s1 = {x for x in 'ablaablalabla' if x not in 'a'}
    print(s1)
    
    
if __name__=='__main__':
    main()