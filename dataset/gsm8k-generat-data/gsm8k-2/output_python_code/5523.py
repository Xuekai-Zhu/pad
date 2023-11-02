def solution():
    """Gondor is a technician, he earns $10 from repairing a phone and $20 from repairing a laptop. If he was able to repair 3 phones last Monday, 5 phones last Tuesday, 2 laptops on Wednesday, and 4 laptops last Thursday, how much does he earn in total?"""
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