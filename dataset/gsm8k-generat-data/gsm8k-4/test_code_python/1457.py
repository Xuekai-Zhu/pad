def solution():
    """In a rice field, you can get a total of 20 sacks of rice every harvest. If the yield increases by twenty percent after every harvest, what is the total number of sacks of rice you can get after the first and second harvest?"""
    # Define the initial yield and the percentage increase per harvest
    initial_yield = 20
    percentage_increase = 0.2

    # Calculate the yield after the first harvest
    yield_1 = initial_yield * (1 + percentage_increase)

    # Calculate the yield after the second harvest
    yield_2 = yield_1 * (1 + percentage_increase)

    # Calculate the total yield after both harvests
    total_yield = initial_yield + yield_1 + yield_2

    # return the result
    result = total_yield
    return result

print(solution())