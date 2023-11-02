def solution():
    """In a rice field, you can get a total of 20 sacks of rice every harvest. If the yield increases by twenty percent after every harvest, what is the total number of sacks of rice you can get after the first and second harvest?"""
    harvest1_yield = 20
    harvest2_yield = harvest1_yield * 1.2
    total_yield = harvest1_yield + harvest2_yield
    result = total_yield
    return result

print(solution())