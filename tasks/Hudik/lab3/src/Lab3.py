
N1 = 363542076673
N2 = 728740902979
N3 = 522993716719
C1 = 246562834516
C2 = 291375746601
C3 = 222724269731
e = 3


M0 = N1 * N2 * N3
print(f"M0 =", M0) #138555669564008119302694433926047373

m1 = N2 * N3
m2 = N1 * N3
m3 = N1 * N2
print(f"m1 =", m1) #381126913374147389205901
print(f"m2 =", m2) #190130221862955939995887
print(f"m3 =", m3) #264927981225542872108867

n1 = pow(m1, -1, N1)
n2 = pow(m2, -1, N2)
n3 = pow(m3, -1, N3)
print(f"n1 =", n1) #287993142707
print(f"n2 =", n2) #106614970676
print(f"n3 =", n3) #32171022265

S = C1 * n1 * m1 + C2 * n2 * m2 + C3 * n3 * m3
print(f"S =", S) 

M = round(pow((S % M0), (1/e)))
print(f"M =", M) 
