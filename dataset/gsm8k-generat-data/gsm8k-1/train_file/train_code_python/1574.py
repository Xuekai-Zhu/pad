def solution():
    """After shearing her 200 sheep, Azalea paid the shearer who had come to help her with the work $2000 for his job. Each of the sheared sheep produced 10 pounds of wool. If Ms. Azalea sold a pound of wool at $20, how much profit did she make from the produce of her sheep farm?"""
    num_sheep = 200
    wool_per_sheep = 10
    total_wool = num_sheep * wool_per_sheep
    price_per_pound = 20
    total_income = total_wool * price_per_pound
    expenses = 2000
    profit = total_income - expenses
    result = profit
    return result

print(solution())