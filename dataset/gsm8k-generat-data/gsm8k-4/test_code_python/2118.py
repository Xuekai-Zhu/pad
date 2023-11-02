def solution():
    """Brandon has been fired from half the businesses in town and has quit from a third of them. If there are 72 business in town, how many businesses can he still apply to?"""
    # Define the total number of businesses in town
    total_businesses = 72
    
    # Calculate the number of businesses Brandon has been fired from
    fired_businesses = total_businesses / 2
    
    # Calculate the number of businesses Brandon has quit from
    quit_businesses = total_businesses / 3
    
    # Calculate the number of businesses Brandon can still apply to
    remaining_businesses = total_businesses - fired_businesses - quit_businesses
    
    # return the result
    result = remaining_businesses
    return result

print(solution())