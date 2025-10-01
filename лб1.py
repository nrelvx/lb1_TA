import math

def ring(R1, R2):
    if R1<0 or R2<=R1:
        print("Помилка, введіть інше значення")
        return None
    S = math.pi * (R2**2 - R1**2)
    return S
R1=float(input("Введіть внутрішній радіус: "))
R2=float(input("Введіть зовнішній радіус: "))

result=ring(R1, R2)
if result is not None:
    print(f"Площа кільця S = {result}")
