def solution():
    total_points = 100  # The threshold to go to the office is 100 points
    interrupt_points = 5  # Jerry gets 5 points for each interruption
    insult_points = 10  # Jerry gets 10 points for each insult
    throw_points = 25  # Jerry gets 25 points for each item he throws

    # Calculate the points Jerry has accumulated so far
    jerry_points = interrupt_points * 2 + insult_points * 4

    # Calculate the points Jerry can still accumulate
    remaining_points = total_points - jerry_points

    # Calculate the number of times Jerry can still throw things
    throws_possible = remaining_points // throw_points
    result = throws_possible
    return result

print(solution())