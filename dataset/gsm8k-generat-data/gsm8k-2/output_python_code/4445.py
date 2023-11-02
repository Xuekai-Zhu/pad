def solution():
    """Hans reserved a table at a fine dining restaurant for twelve people. He has to pay a deposit for the reservation, and the deposit is a flat $20 plus an extra $3 per adult but only $1 per child. Two of the people in Hans’s party are his kid cousins, and the rest are adults. How many dollars does Hans have to pay as a deposit for the restaurant reservation?"""
    num_adults = 10 # 12 total people with 2 kid cousins
    num_children = 2
    deposit = 20 + (3 * num_adults) + (1 * num_children)
    result = deposit
    return result

print(solution())