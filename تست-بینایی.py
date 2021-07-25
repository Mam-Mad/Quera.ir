"""
Question:
https://quera.ir/problemset/contest/2659/سؤال-تست-بینایی
"""

a = int(input())
true = input()
false = input()

mistake = 0
for i in range(0,a):
    if true[i] != false[i]:
        mistake += 1

print(mistake)
