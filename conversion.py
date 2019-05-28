def decimalToRep(n,r):
    if r==16:
        return hex(n)[2:]
    elif r==10:
        return str(n)
    elif r==8:
        return oct(n)[2:]
    elif r==2:
        return bin(n)[2:]
    else:
        return 'base should be (2,8,10,16)'
def main():
    print(decimalToRep(10,10))
    print(decimalToRep(10,8))
    print(decimalToRep(10,2))
    print(decimalToRep(10,16))




if __name__=='__main__':
    main()
