def solution():
    """Barry wants to make a huge salad using only cucumbers and tomatoes. He will use a total of 280 pieces of vegetables. If there are thrice as many tomatoes as cucumbers, how many cucumbers will be used in the salad?"""
    # Define the total number of vegetables
    total_vegetables = 280
    
    # Define the ratio of tomatoes to cucumbers
    tomato_cucumber_ratio = 3
    
    # Calculate the total number of parts in the ratio
    total_ratio_parts = 4  # (3 parts tomatoes + 1 part cucumbers)
    
    # Calculate the number of parts per cucumber
    cucumber_parts = 1 / total_ratio_parts
    
    # Calculate the number of cucumbers
    cucumber_count = total_vegetables * cucumber_parts
    
    result = cucumber_count
    return result

print(solution())