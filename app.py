










tuition =8000

print("Year \tTuition")


for x in range(1, 6):
    tuition += tuition* 0.03
    print(x, "\t\t$", format(tuition, '.2f'))


salary =200000

print("Year \tSalary")


for x in range(1, 11):
    salary += salary * 0.03
    print(x, "\t\t$", format(tuition, '.2f'))