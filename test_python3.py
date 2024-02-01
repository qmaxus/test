import re

def add_atm_machine(n:int,k: int,l: list)-> list:
    """
    :param n: Number of ATMs available
    :param k: Required Number of ATMs to add
    :param l: Distance between ATMs
    :return: List of new distances between ATMs
    """
    arr = []
    if n==len(l)+1:
        h ={l1:[l1,1] for l1 in l}
        for v  in range(k):
            l = sorted(h,  key=lambda x: h[x][0]/h[x][1], reverse=True)
            h[l[0]][1]+=1
        arr = [round(f[0]/f[1],1) for _,f in h.items() for _ in range(f[1])]
    return arr


def check_single(x,r):
    return x.ljust(r,'9') if x.isdigit() else ''

def maximum_possible_number(l:list)->int:
    """
    :param l: List of strings consisting of digits
    :return: Returns the maximum possible number
    """
    arr = sorted(l, key=lambda x: check_single(x, len(max(l, key=len))), reverse=True)
    return int(''.join([val for val in arr if val.isdigit()]))

def seart_number(text: str)->str:
    """
    :param text:  Parsing text
    :return: Good number padded with zeros to the left of both numbers
    """
    template = ''
    for s in re.finditer('[\d]+\\\[\d]+', text):
        if s is not None:
            t= s.group().split('\\')
            if len(t)==2:
                if 2<=len(t[0])<=4 and 2<=len(t[0])<=5:
                    template += f'{ t[0].rjust(4,"0")}\\{ t[1].rjust(5,"0")} '

    return template

# 3 Тестовые задания python
if __name__=='__main__':
    #Test1
    print(seart_number('Адрес5467\\456. Номер 405\\549'))

    #Test 2
    print(add_atm_machine(5, 3, [100,23,34,80]))

    #Test 3
    print(maximum_possible_number(['89','41','4','005','ttt']))



