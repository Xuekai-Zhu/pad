def solution():
    """In a rice field, you can get a total of 20 sacks of rice every harvest. If the yield increases by twenty percent after every harvest, what is the total number of sacks of rice you can get after the first and second harvest?"""
    # Define the initial number of sacks of rice per harvest
    INITIAL_YIELD = 20

    # Calculate the yield after the first harvest
    yield_after_first_harvest = INITIAL_YIELD * 1.2

    # Calculate the yield after the second harvest
    yield_after_second_harvest = yield_after_first_harvest * 1.2

    # Calculate the total number of sacks of rice after the two harvests
    total_yield = INITIAL_YIELD + yield_after_first_harvest + yield_after_second_harvest

    # Display the total yield
    result = total_yield
    return result

print(solution())