def solution():
    """Barry wants to make a huge salad using only cucumbers and tomatoes. He will use a total of 280 pieces of vegetables. If there are thrice as many tomatoes as cucumbers, how many cucumbers will be used in the salad?"""
    total_veggies = 280
    tomato_ratio = 3
    total_ratio = 4
    cucumber_ratio = total_ratio - tomato_ratio
    total_parts = tomato_ratio + cucumber_ratio
    cucumber_count = (cucumber_ratio / total_parts) * total_veggies
    result = cucumber_count
    return result

print(solution())