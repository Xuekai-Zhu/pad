def solution():
    """In a hotdog eating competition, the first competitor can eat 10 hot dogs per minute. The second competitor can eat 3 times more than the first competitor, while the third competitor can eat twice as much as the second competitor. How many hotdogs can the third competitor eat after 5 minutes?"""
    # Define the eating rates of each competitor
    competitor_1_rate = 10
    competitor_2_rate = 3 * competitor_1_rate
    competitor_3_rate = 2 * competitor_2_rate

    # Calculate the number of hot dogs each competitor can eat in 5 minutes
    competitor_1_dogs = competitor_1_rate * 5
    competitor_2_dogs = competitor_2_rate * 5
    competitor_3_dogs = competitor_3_rate * 5

    # Return the number of hot dogs the third competitor can eat in 5 minutes
    result = competitor_3_dogs
    return result

print(solution())