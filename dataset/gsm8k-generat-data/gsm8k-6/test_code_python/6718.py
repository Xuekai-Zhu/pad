def solution():
    # Calculate the total amount of shampoo Janet has
    total_shampoo = 1/3 + 1/4  # in units of a bottle
    total_shampoo *= 12  # convert to units of 1/12 bottle

    # Calculate the number of days her shampoo will last
    days_last = total_shampoo / (1/12)  # she uses 1/12 of a bottle per day
    result = days_last
    return result

print(solution())