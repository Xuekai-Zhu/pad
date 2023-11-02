def solution():
    
    phone_income = 10
    laptop_income = 20
    monday_income = 3 * phone_income
    tuesday_income = 5 * phone_income
    wednesday_income = 2 * laptop_income
    thursday_income = 4 * laptop_income
    total_income = monday_income + tuesday_income + wednesday_income + thursday_income
    result = total_income
    return result

print(solution())