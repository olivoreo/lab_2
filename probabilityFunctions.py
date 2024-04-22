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

def task1_lab2(A):
    if (len(A) != 6):
        return "Введены не все данные!"
    for val in A:
        if (not checkProbability(val)):
            return "Вероятности должны быть в интервале [0,1]"
    return round((1-A[2]) * (1-A[0]) * ((1-A[1]) + (1-A[3]) * (1-A[4]) * (1-A[5]) - (1-A[1]) * (1-A[3]) * (1-A[4]) * (1-A[5])), roundParam)

def totalProbability (H, A):
    if (sum(H) != 1):
        return "Сумма вероятностей гипотез должна равняться 1!"
    value = 0
    for i in range(len(H)):
        value += H[i] * A[i]
    return round(value, roundParam)
def formulaBayes (H, A, I):
    if (sum (H) != 1):
        return "Сумма вероятностей гипотез должна равняться 1!"
    res = dict()
    totalProb = totalProbability(H,A)
    for i in range(len(I)):
        if I[i]:
            res[i] = round((H[i] * A[i]) / totalProb, roundParam)
    return res
def convertResultBayes(resDict, line, startIndex = 0):
    if type(resDict) == str:
        return resDict

    res = ""
    num = line.count('%')
    for key in resDict.keys():
        l = tuple([key + startIndex]*num)
        res += '\n' + line % l + str(resDict[key])
    return res

def Task2_Lab2(P):
    if (len(P) != 5):
        return "Введены не все данные!"

    res = ""
    res += ("\na) P(A1) = " + str(round(P[0]*(1-P[1])*(1-P[2])*(1-P[3])*(1-P[4]), roundParam)) + "; P(A2) = " + str(round((1-P[0])*P[1]*(1-P[2])*(1-P[3])*(1-P[4]), roundParam)))
    res += ("; P(A3) = " + str(round((1 - P[0]) * (1-P[1]) * P[2] * (1 - P[3]) * (1 - P[4]), roundParam)) + "; P(A4) = " + str(round((1 - P[0]) * (1-P[1]) * (1 - P[2]) * P[3] * (1 - P[4]), roundParam)))
    res += ("; P(A5) = " + str(round((1 - P[0]) * (1-P[1]) * (1 - P[2]) * (1 - P[3]) * P[4], roundParam)))

    res += ("\nb) " + str(round(P[0]*(1-P[1])*(1-P[2])*(1-P[3])*(1-P[4]) + (1-P[0])*P[1]*(1-P[2])*(1-P[3])*(1-P[4]) +
                                (1 - P[0]) * (1-P[1]) * P[2] * (1 - P[3]) * (1 - P[4]) + (1 - P[0]) * (1-P[1]) * (1 - P[2]) * P[3] * (1 - P[4]) +
                                (1 - P[0]) * (1-P[1]) * (1 - P[2]) * (1 - P[3]) * P[4], roundParam)))

    res += ("\nc) " + str(round(P[0]*P[1]*(1-P[2])*(1-P[3])*(1-P[4]) + P[0]*(1-P[1])*P[2]*(1-P[3])*(1-P[4]) +
                                P[0] * (1-P[1]) * (1-P[2]) * P[3] * (1 - P[4]) + P[0] * (1-P[1]) * (1 - P[2]) * (1-P[3]) * P[4] +
                                (1 - P[0]) * P[1] * P[2] * (1 - P[3]) * (1-P[4]) +
                                (1 - P[0]) * P[1] * (1-P[2]) * P[3] * (1-P[4]) + (1 - P[0]) * P[1] * (1-P[2]) * (1 - P[3]) * P[4] +
                                (1 - P[0]) * (1-P[1]) * P[2] * P[3] * (1-P[4]) + (1 - P[0]) * (1-P[1]) * P[2] * (1-P[3]) * P[4] +
                                (1 - P[0]) * (1-P[1]) * (1-P[2]) * P[3] * P[4], roundParam)))

    res += ("\nd) " + str(round(P[0]*P[1]*P[2]*P[3]*P[4] + (1-P[0])*P[1]*P[2]*P[3]*P[4] +
                                P[0]*(1-P[1])*P[2]*P[3]*P[4] + P[0]*P[1]*(1-P[2])*P[3]*P[4] +
                                P[0]*P[1]*P[2]*(1-P[3])*P[4] + P[0]*P[1]*P[2]*P[3]*(1-P[4]), roundParam)))

    res += ("\ne) " + str(round(1 - ((1-P[0])*(1-P[1])*(1-P[2])*(1-P[3])*(1-P[4])), roundParam)))


    return res