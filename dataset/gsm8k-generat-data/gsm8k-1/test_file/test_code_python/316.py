There are two parts to this problem, so here's a solution for each part:

Part 1:
def solution():
    """At the beginning of the party, there were 25 men and 15 women. After an hour, 1/4 of the total number of people left. How many people are left after an hour?"""
    men_at_start = 25
    women_at_start = 15
    total_at_start = men_at_start + women_at_start
    fraction_left = 3/4
    total_left = total_at_start * fraction_left
    result = total_left
    return result

Part 2:
def solution():
    """If 22 men stayed at the party after 1/4 of the total number of people left, how many women are left?"""
    men_left = 22
    total_left = solution_part_1() # calling the solution for Part 1
    women_left = total_left - men_left
    result = women_left
    return result

print(solution())