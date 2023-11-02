def solution():
    
    monday_seashells = 30
    tuesday_seashells = monday_seashells / 2
    total_seashells = monday_seashells + tuesday_seashells
    selling_price = 1.20
    total_income = total_seashells * selling_price
    result = total_income
    return result

print(solution())