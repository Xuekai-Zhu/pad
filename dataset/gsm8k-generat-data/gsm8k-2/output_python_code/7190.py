def solution():
    """Sally picks 30 seashells on Monday. On Tuesday, she picks half as many seashells as she did on Monday. If she can sell each seashell for $1.20, how much money can she make if she sells all of her seashells?"""
    monday_seashells = 30
    tuesday_seashells = monday_seashells / 2
    total_seashells = monday_seashells + tuesday_seashells
    selling_price = 1.20
    total_income = total_seashells * selling_price
    result = total_income
    return result

print(solution())