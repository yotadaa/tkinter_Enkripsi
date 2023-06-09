import random

'''ASCII = []

    for i in range(256):
        ASCII.append(chr(i))'''
def processes(plainText):

    ASCII = []

    for i in range(256):
        ASCII.append(chr(i))
    poq = len(ASCII)
    def prima(n):
        if n == 1:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def get_p():
        a = random.choice(range(2**10))
        if prima(a):
            return a
        else:
            return get_p()

    def get_q():
        a = random.choice(range(2**10))
        if prima(a):
            if prima(a) == p:
                return get_q()
            else:
                return a
        else:
            return get_q()

    def getE(r1,r2,nilai):
        qq = r1//r2
        r3 = r1 - (qq*r2)
        nilai.append(r3)
        if r3 != 0:
            return getE(r2,r3,nilai)

    def search(totien):
        e = random.choice(range(1,totien-1))
        nilai = []
        peak = getE(e,totien,nilai)
        if nilai[len(nilai)-2] == 1:
            return e
        else:
            return search(totien)
        
    def getK(ee,totien):
        k = 1
        while True:
            d,r = divmod(k*totien+1,ee)
            if r == 0:
                return d
            k+=1
        
        
        
    #1
    p = get_p()
    q = get_q()
    #2
    N = p * q
    #3
    m = (p-1)*(q-1)
    #4
    E = search(m)
    #5
    d = getK(E,m)

    #6
    pbkey = (E,N)
    pvkey = (d,N)

    text = plainText
    text_in_ascii = []
    for i in range(len(text)):
        text_in_ascii.append(ASCII.index(text[i]))
        
    encryptedText = [(i**E % N) for i in text_in_ascii]

    return (encryptedText,d,N)
