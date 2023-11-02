def solution():
    # Calculate the number of adults in Hans's party
    num_adults = 12 - 2  # two of the people in Hans's party are children

    # Calculate the deposit amount based on the number of adults and children
    deposit = 20 + 3*num_adults + 1*2  # $3 per adult, $1 per child

    result = deposit
    return result

print(solution())