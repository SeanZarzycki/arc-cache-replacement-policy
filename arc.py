
import string

t1 = ['x','y','a','d'] # LRU->MRU
b1 = []
t2 = []
b2 = []
p = 0
c = 4
l1 = [t1, b1]
l2 = [t2, b2]
def len_sum(lists):
    sum = 0
    for l in lists:
        sum += len(l)
    return sum

def remove_page(l,page):
    l.remove(page)

def safediv(x,y):
    if y == 0.0:
        return 0.0
    else:
        return float(x)/float(y)

def replace(x):
    global p
    global t1
    global t2
    if len(t1) >= 1 and ((x in b2 and len(t1) == p) or len(t1) > p):
        b1.append(t1[0])
        t1 = t1[1:]
    else:
        b2.append(t2[0])
        t2 = t2[1:]

def dbl_insert(x):
    global p
    global c
    # case 1
    if x in t1:
        remove_page(t1,x)
        t2.append(x)
    elif x in t2:
        remove_page(t2,x)
        t2.append(x)
    # case 2
    elif x in b1:
        p = min(c, p + max(safediv(len(b2),len(b1)),1))
        replace(x)
        t2.append(x)
        b1.remove(x)
    # case 3
    elif x in b2:
        p = max(0, p - max(safediv(len(b1),len(b2)),1))
        replace(x)
        t2.append(x)
        b2.remove(x)

    #case 4
    else:
        l1_len = len(t1) + len(b1)
        l2_len = len(t2) + len(b2)
        if l1_len == c: # case i
            if len(t1) < c:
                b1.pop()
                replace(x)
            else:
                t1.pop()
        elif l1_len < c and l1_len + l2_len >= c: # case ii
            if l1_len + l2_len == 2*c:
                b2.pop()
            replace(x)
        t1.append(x)
    

elems = 'abcddeac'
for e in list(elems):
    print 'inserting ', e
    dbl_insert(e)
    print 'p = ', p,'t1 = ',t1,'b1 = ',b1,'t2 = ',t2,'b2 = ',b2