roundParam = 10
def checkProbability (val):
    return 0 <= val <= 1
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

def combWithoutRep(n, m):
    if (n >= m):
        return int(factorial(n) // (factorial(m) * factorial(n - m)))
    else:
        return -1


def placeWithoutRep(n, m):
    if (n >= m):
        return int(factorial(n) // factorial(n - m))
    else:
        return -1


def combWithRep(n, m):
    return combWithoutRep(n + m - 1, m)


def placeWithRep(n, m):
    return n ** m


def permutationsWithRep(mList):
    n = sum(mList)
    value = factorial(n)
    for m in mList:
        value = value // factorial(m)
    return int(value)

def task2_lab1(n, m):
    if n>=m:
        return round(1/combWithoutRep(n,m),17)
    else:
        return -1

def task4_lab1(nList):
    value = permutationsWithRep(nList)
    value = value / placeWithRep(len(nList), sum(nList))
    return value

def task5_lab1(kList, nList, N):
    res = 1
    if len(kList)!=len(nList):
        return -1
    for i in range(len(kList)):
        k = kList[i]
        n = nList[i]
        res = res * combWithoutRep(k,n)
        if (res < 0):
            return -1
    res = res / combWithoutRep(sum(kList), N)
    return res
def task1_lab2(A):
    if (len(A) != 5):
        return -1
    for val in A:
        if (not checkProbability(val)):
            return -1
    return round((A[0] + A[3] - (A[0] * A[3])) * A[2] * (A[1] + A[4] - (A[1] * A[4])), roundParam)
def totalProbability (H, A):
    if (len(H)!=len(A) or sum(H) != 1):
        return -1
    value = 0
    for i in range(len(H)):
        value += H[i] * A[i]
    return round(value, roundParam)
def formulaBayes (H, A, I):
    if (len(H) != len(A) != len(I) or sum (H) != 1):
        return -1
    res = dict()
    totalProb = totalProbability(H,A)
    for i in range(len(I)):
        if I[i]:
            res[i] = round((H[i] * A[i]) / totalProb, roundParam)
    return res
def convertResultBayes(resDict, line, startIndex = 0):
    res = ""
    num = line.count('%')
    for key in resDict.keys():
        l = tuple([key + startIndex]*num)
        res += '\n' + line % l + str(resDict[key])
    return res

def MProbability_Task2_Lab2(n, m):
    numerator = ((combWithoutRep(n - m,1 ) * combWithoutRep(m, 2)) + (combWithoutRep(n - m, 0) * combWithoutRep(m,3)))
    denominator = combWithoutRep(n,3)
    return round(numerator / denominator, roundParam)

def Task2_1_Lab2(n,m1,m2):
    return round(MProbability_Task2_Lab2(n,m1) * MProbability_Task2_Lab2(n, m2), roundParam)

def Task2_2_Lab2(n,m1,m2):
    return round(MProbability_Task2_Lab2(n,m1) * (1 - MProbability_Task2_Lab2(n, m2)), roundParam)

def Task2_3_Lab2(n,m1,m2):

    return round((MProbability_Task2_Lab2(n,m1) * (1 - MProbability_Task2_Lab2(n, m2))) + (1 - MProbability_Task2_Lab2(n,m1)) * MProbability_Task2_Lab2(n, m2), roundParam)

def Task2_4_Lab2(n,m1,m2):
    return round(MProbability_Task2_Lab2(n,m1) + MProbability_Task2_Lab2(n, m2) - (MProbability_Task2_Lab2(n,m1) * MProbability_Task2_Lab2(n, m2)), roundParam)

def Task2_Lab2(n,m1,m2):
    if n < 0 or m1 < 0 or m2 < 0 :
        return -1
    res = ""
    res += "\nP(A1) = " + str(MProbability_Task2_Lab2(n, m1))
    res += "\nP(A2) = " + str(MProbability_Task2_Lab2(n, m2))
    res += "\na) " + str(Task2_1_Lab2(n, m1, m2))
    res += "\nb) " + str(Task2_2_Lab2(n, m1, m2))
    res += "\nc) " + str(Task2_3_Lab2(n, m1, m2))
    res += "\nd) " + str(Task2_4_Lab2(n, m1, m2))
    return res