"""
Question:
https://quera.ir/contest/assignments/915/problems/3085
"""


WeightInKilograms = float(input())
HeightInMeters = float(input())

BMI = WeightInKilograms / (HeightInMeters*HeightInMeters)
print(round(BMI, 2))

if BMI < 18.5:
    print("Underweight")
elif  18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")
