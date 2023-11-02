def solution():
    """Dilan, Martha, Phillip, and Veronica went to the park together to have some fun. They all had a different number of marbles: Dilan had 14 marbles, Martha had 20 marbles, Phillip had 19 marbles and finally, Veronica had only 7 marbles. They wanted to redistribute the marbles so they each had an equal number. How many marbles did each friend have at the end of the day?"""
    total_marbles = 14 + 20 + 19 + 7
    num_friends = 4
    equal_marbles = total_marbles / num_friends
    result = equal_marbles
    return result

print(solution())