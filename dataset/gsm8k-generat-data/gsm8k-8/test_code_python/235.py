def solution():
    # Define the number of trains Max gets each year
    birthday_gifts = 1
    christmas_gifts = 2

    # Calculate the total number of trains Max receives over 5 years
    total_gifts = (birthday_gifts * 5) + (christmas_gifts * 5)

    # Calculate the number of trains Max has at the end of 5 years
    starting_trains = total_gifts
    ending_trains = starting_trains * 2
    
    result = ending_trains
    return result

print(solution())