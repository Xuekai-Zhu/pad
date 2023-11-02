def solution():
    """Hans reserved a table at a fine dining restaurant for twelve people. He has to pay a deposit for the reservation, and the deposit is a flat $20 plus an extra $3 per adult but only $1 per child. Two of the people in Hans’s party are his kid cousins, and the rest are adults. How many dollars does Hans have to pay as a deposit for the restaurant reservation?"""
    # Define the number of adults and children in Hans' party
    num_adults = 10
    num_children = 2

    # Define the deposit amounts per adult and per child
    deposit_per_adult = 3
    deposit_per_child = 1

    # Calculate the total deposit amount
    total_deposit = 20 + (num_adults * deposit_per_adult) + (num_children * deposit_per_child)

    # Display the total deposit amount
    result = total_deposit
    return result

print(solution())