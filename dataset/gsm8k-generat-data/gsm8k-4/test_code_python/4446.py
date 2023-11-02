def solution():
    """Hans reserved a table at a fine dining restaurant for twelve people. He has to pay a deposit for the reservation, and the deposit is a flat $20 plus an extra $3 per adult but only $1 per child. Two of the people in Hans’s party are his kid cousins, and the rest are adults. How many dollars does Hans have to pay as a deposit for the restaurant reservation?"""
    # Define the number of adults and children in the party
    adults = 10
    children = 2

    # Calculate the deposit for the adults and children separately
    adult_deposit = adults * 3
    child_deposit = children * 1

    # Calculate the total deposit
    total_deposit = 20 + adult_deposit + child_deposit

    # Return the result
    result = total_deposit
    return result

print(solution())