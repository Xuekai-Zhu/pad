def solution():
    total_yield = 20  # You can get a total of 20 sacks of rice every harvest
    increase_percent = 20  # The yield increases by 20% after every harvest

    # Calculate the yield after the first harvest
    first_harvest_yield = total_yield + (total_yield * (increase_percent/100))

    # Calculate the yield after the second harvest
    second_harvest_yield = first_harvest_yield + (first_harvest_yield * (increase_percent/100))

    # Calculate the total number of sacks of rice you can get after the first and second harvest
    total_yield_after_two_harvests = total_yield + first_harvest_yield + second_harvest_yield

    result = total_yield_after_two_harvests
    return result

print(solution())