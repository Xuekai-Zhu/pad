def solution():
    cakes_per_day = 5 - 1  # Julia bakes one less than 5 cakes per day
    days = 6  # Julia bakes for 6 days

    # Calculate the total number of cakes Julia bakes
    total_cakes = cakes_per_day * days

    # Calculate the number of cakes eaten by Clifford
    eaten_cakes = (days // 2)  # Clifford eats one cake every other day

    # Calculate the number of cakes Julia has remaining
    remaining_cakes = total_cakes - eaten_cakes
    result = remaining_cakes
    return result

print(solution())