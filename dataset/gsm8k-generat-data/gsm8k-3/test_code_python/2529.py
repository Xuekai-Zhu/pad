def solution():
    """In a hotdog eating competition, the first competitor can eat 10 hot dogs per minute. The second competitor can eat 3 times more than the first competitor, while the third competitor can eat twice as much as the second competitor. How many hotdogs can the third competitor eat after 5 minutes?"""
    # Define the first competitor's eating rate
    competitor1_rate = 10 

    # Define the second competitor's eating rate as three times that of the first competitor
    competitor2_rate = competitor1_rate * 3 

    # Define the third competitor's eating rate as twice that of the second competitor
    competitor3_rate = competitor2_rate * 2 

    # Calculate the total number of hotdogs eaten by the third competitor after 5 minutes
    total_hotdogs = competitor3_rate * 5 

    # Display the total number of hotdogs eaten
    result = total_hotdogs
    return result

print(solution())