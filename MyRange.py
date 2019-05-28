def myrange(inp):
    if len(inp)<3:
        inp+=[None]*(3-len(inp))
    start,stop,inc=inp
    l = []
    if (start==None and stop==None and inc==None):
        return 'invalid arguments '
    elif stop ==None and inc==None:
        stop = start
        start=0
        inc=1
    elif  inc==None:
        inc=1
    else:
        if  ((start > stop) and inc > -1) or((start <stop) and inc<0):
            return 'Invalid arguments'


    if stop>start:
        while start<stop:
            l.append(start)
            start+=inc
    else:
        while start>stop:
            l.append(start)
            start+=inc
    return  l

if __name__=='__main__':
    inp=list(map(int,input('Enter start stop inc:').split()))
    print(myrange(inp))