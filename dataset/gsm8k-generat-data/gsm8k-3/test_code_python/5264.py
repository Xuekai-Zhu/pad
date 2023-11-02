def solution():
    """In preparation for the church fundraiser, Julia bakes one less than 5 cakes per day for 6 days.  Unfortunately, every other day, Julia's brother, Clifford, sneaks into Julia's house and eats one of Julia's cakes.  At the end of 6 days, how many cakes does Julia have remaining?"""
    
    # Define the number of cakes Julia bakes each day
    num_cakes = 4
    
    # Define the number of days Julia bakes
    num_days = 6
    
    # Calculate the total number of cakes Julia bakes
    total_cakes = num_cakes * num_days
    
    # Calculate the number of cakes Clifford eats
    clifford_cakes = num_days // 2
    
    # Calculate the number of cakes Julia has left
    remaining_cakes = total_cakes - clifford_cakes
    
    # Display the number of cakes Julia has remaining
    result = remaining_cakes
    return result

print(solution())