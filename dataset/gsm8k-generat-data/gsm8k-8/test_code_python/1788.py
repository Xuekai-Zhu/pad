def solution():
    # Calculate the number of lychees sold
    lychees_sold = 500 / 2

    # Calculate the number of lychees taken home
    lychees_taken_home = 500 - lychees_sold

    # Calculate the number of lychees eaten
    lychees_eaten = lychees_taken_home * 3/5

    # Calculate the number of lychees remaining
    lychees_remaining = lychees_taken_home - lychees_eaten

    result = lychees_remaining
    return result

print(solution())