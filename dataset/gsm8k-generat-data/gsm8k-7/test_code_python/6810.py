def solution():
    num_cakes_per_day = 20
    num_days = 9

    # Calculate the total number of cakes Brenda bakes
    total_cakes_baked = num_cakes_per_day * num_days

    # Calculate the number of cakes Brenda sells
    num_cakes_sold = total_cakes_baked / 2

    # Calculate the number of cakes remaining with Brenda
    num_cakes_left = total_cakes_baked - num_cakes_sold
    result = num_cakes_left
    return result

print(solution())