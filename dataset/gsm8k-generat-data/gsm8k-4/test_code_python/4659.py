def solution():
    """There are 48 passengers on the bus. Two-thirds of the passengers are women and the rest are men. If one-eighth of the men are standing, how many men are seated?"""
    # Define the total number of passengers
    total_passengers = 48

    # Calculate the number of women on the bus
    women_passengers = total_passengers * (2/3)

    # Calculate the number of men on the bus
    men_passengers = total_passengers - women_passengers

    # Calculate the number of men who are standing
    standing_men = men_passengers / 8

    # Calculate the number of men who are seated
    seated_men = men_passengers - standing_men

    # Return the result
    result = seated_men
    return result

print(solution())