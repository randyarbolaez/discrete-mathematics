import random
# a = qb + r | [0 <= r < b] | b >0
# a = dividend
# q = quotient
# b = divisor
# r = remainder

# a = 43
# b = 4
# q = 10

ifUserWouldLikeToRandomizeValues = int(float(input("Would you like to randomize values? (1: yes | 2: no): ")))
while ifUserWouldLikeToRandomizeValues != 1 and ifUserWouldLikeToRandomizeValues != 2:
        ifUserWouldLikeToRandomizeValues = int(float(input("Would you like to randomize values? (1: yes | 2: no): ")))

if ifUserWouldLikeToRandomizeValues == 1:
        a = random.randint(0, 9999999999)
        b = random.randint(0, 9999999999)
else:
        a = int(float(input("Enter value: ")))
        b = int(input("Enter positive value: "))

while b<0:
        print("\nPlease enter a positive value.")
        b = int(input("Positive value: "))
q = 0
r = 0

if isinstance((a/b), float):
        q= int(a/b)
        if a<0:
                q-=1
        r = (a-(q*b))

print(f'\ndivisor:{b} | dividend:{a}')
if r == 0:
        print(f'\n{b} | {a} = {a/b}')
else:
        print("\nThe quotient is: " + str(q) + " with a remainder is " + str(r))