def solution():
    # Define the number of electoral votes for Ronald Reagan and Jimmy Carter
    reagan_electoral_votes = 489
    carter_electoral_votes = 49
    # Check if the difference in electoral votes is less than or equal to the number of states won by Jimmy Carter
    if abs(reagan_electoral_votes - carter_electoral_votes) <= 6:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())