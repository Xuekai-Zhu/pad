def solution():
    """In a rice field, you can get a total of 20 sacks of rice every harvest. If the yield increases by twenty percent after every harvest, what is the total number of sacks of rice you can get after the first and second harvest?"""
    harvest_one = 20
    harvest_two = harvest_one * 1.2
    total_harvest = harvest_one + harvest_two
    result = total_harvest
    return result

print(solution())