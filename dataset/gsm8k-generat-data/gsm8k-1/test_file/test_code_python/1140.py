def solution():
    """The ratio of men to women on a bus is 5:9. If the total number of passengers on the bus is 84, and 20 women alight from the bus at the next stop, how many women have remained on the bus?"""
    ratio_men_to_women = 5/9
    total_passengers = 84
    women_passengers = total_passengers * (9/14)
    women_remaining = women_passengers - 20
    result = women_remaining
    return result

(Note: The solution for this problem was not given in the original prompt, so I provided one here.)

print(solution())