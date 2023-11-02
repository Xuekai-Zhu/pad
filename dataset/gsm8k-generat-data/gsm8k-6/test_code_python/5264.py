def solution():
    # Calculate the total number of cakes baked by Julia
    total_cakes = 4 * 6  # Julia bakes one less than 5 cakes per day for 6 days

    # Calculate the number of cakes eaten by Clifford
    cakes_eaten = 3  # Every other day, Clifford eats one of Julia's cakes

    # Calculate the number of cakes remaining with Julia
    cakes_remaining = total_cakes - cakes_eaten

    result = cakes_remaining
    return result

print(solution())