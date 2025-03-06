from cmath import sqrt
first_kat = int(input("Enter first kat: "))
second_kat = int(input("Enter second kat: "))
gipotenus = sqrt(first_kat**2 + second_kat**2)
s = ((first_kat * second_kat) / 2)

print("Hypotenuse =", gipotenus)
print("S =",s)