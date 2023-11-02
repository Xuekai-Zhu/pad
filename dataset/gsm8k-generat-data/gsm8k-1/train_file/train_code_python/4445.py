def solution():
    """Hans reserved a table at a fine dining restaurant for twelve people. He has to pay a deposit for the reservation, and the deposit is a flat $20 plus an extra $3 per adult but only $1 per child. Two of the people in Hans’s party are his kid cousins, and the rest are adults. How many dollars does Hans have to pay as a deposit for the restaurant reservation?"""
    adult_count = 10
    child_count = 2
    adult_deposit = 3
    child_deposit = 1
    flat_deposit = 20
    total_deposit = flat_deposit + (adult_count * adult_deposit) + (child_count * child_deposit)
    result = total_deposit
    return result

print(solution())