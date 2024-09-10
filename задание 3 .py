from sys import setrecursionlimit
setrecursionlimit(3000)
def FastSort(mas):
    if len(mas)<2:
        return mas
    else:
        baz_elem=mas[0]
        pred_mas=[]
        for i in range (1,len(mas)):
            n=mas[i]
            if n<=baz_elem:pred_mas.append(n)
        sled_mas=[]
        for i in range (1,len(mas)):
            n=mas[i]
            if n>baz_elem:sled_mas.append(n)
        return FastSort(pred_mas)+[baz_elem]+FastSort(sled_mas)
