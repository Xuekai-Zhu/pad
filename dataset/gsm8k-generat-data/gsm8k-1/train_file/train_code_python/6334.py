def solution():
    """Barry wants to make a huge salad using only cucumbers and tomatoes. He will use a total of 280 pieces of vegetables. If there are thrice as many tomatoes as cucumbers, how many cucumbers will be used in the salad?"""
    total_veggies = 280
    tomato_cucumber_ratio = 3
    total_ratio_parts = 4   # tomato_cucumber_ratio + 1
    cucumber_parts = total_veggies / total_ratio_parts
    cucumbers_used = cucumber_parts
    result = cucumbers_used
    return result

print(solution())