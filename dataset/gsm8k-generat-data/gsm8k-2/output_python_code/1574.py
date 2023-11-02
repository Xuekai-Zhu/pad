def solution():
    """After shearing her 200 sheep, Azalea paid the shearer who had come to help her with the work $2000 for his job. Each of the sheared sheep produced 10 pounds of wool. If Ms. Azalea sold a pound of wool at $20, how much profit did she make from the produce of her sheep farm?"""
    num_sheep = 200
    pay_shearer = 2000
    total_wool = num_sheep * 10
    price_per_pound = 20
    revenue = total_wool * price_per_pound
    profit = revenue - pay_shearer
    result = profit
    return result

print(solution())