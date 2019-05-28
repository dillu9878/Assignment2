def unique(filename='input.txt'):
    f=open(filename,'r')
    s=f.read()

    s=s.split(' ')
    print(s)
    s=list(set(s))
    s.sort()
    for i in s:
        print(i,end=' ')
    return s
if __name__=='__main__':
    filename=input('Enter file name:')
    if filename !='':
        unique(filename)
    else:
        unique()