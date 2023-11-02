def solution():
    """During the hot dog eating contest, the 1st competitor ate 12 hot dogs in 3 minutes.  The 2nd competitor ate twice that amount and the 3rd competitor ate 25% less than the 2nd competitor.  How many hotdogs did the 3rd competitor eat?"""
    # Define the number of hot dogs eaten by the first competitor
    comp1_hotdogs = 12

    # Define the number of hot dogs eaten by the second competitor
    comp2_hotdogs = comp1_hotdogs * 2

    # Define the number of hot dogs eaten by the third competitor
    comp3_hotdogs = comp2_hotdogs * 0.75

    # Display the number of hot dogs eaten by the third competitor
    result = comp3_hotdogs
    return result

print(solution())