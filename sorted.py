def checkSorted(List):
    check=0
    for i in range(1,len(List)):
        if List[i]<List[i-1]:
            check=1
            break
    if check==1:
        return False
    return True

if  __name__=='__main__':
    List=list(map(int,input('Enter List Element:').split()))
    print(checkSorted(List))
