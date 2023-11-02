def solution():
    cakes_per_day = 4  # one less than 5
    num_days = 6

    # Calculate the total number of cakes baked by Julia
    total_cakes = cakes_per_day * num_days

    # On every other day, one cake is eaten by Clifford.
    for i in range(1, num_days+1):
        if i % 2 == 0:  # every other day
            total_cakes -= 1

    # Final number of cakes remaining
    result = total_cakes
    return result

print(solution())