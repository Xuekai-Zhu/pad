def solution():
    ernie_percentage = 4/5
    jack_percentage = 2
    ernie_initial = 6000
    ernie_income = ernie_percentage * ernie_initial
    jack_income = jack_percentage * ernie_initial
    total_income = ernie_income + jack_income
    result = total_income
    return result

print(solution())