def frequency(filename='input.txt'):
    f = open('input.txt', 'r')
    s = f.read()
    s=s.split()
    s.sort()
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    s=sorted(list(set(s)))
    for i in s:
        print('{}:{}'.format(i,freq.get(i)),end=' ')

if __name__=='__main__':
    filename = input('Enter file name:')
    if filename != '':
        frequency(filename)
    else:
        frequency()

