def solution():
    """Levi has 5 lemons. Jayden has 6 more lemons than Levi. Jayden has one-third as many lemons as Eli has while Eli has one-half as many lemons as Ian has. How many lemons do they have in all?"""
    levi_lemons = 5
    jayden_lemons = levi_lemons + 6
    eli_lemons = jayden_lemons * 3
    ian_lemons = eli_lemons * 2
    total_lemons = levi_lemons + jayden_lemons + eli_lemons + ian_lemons
    result = total_lemons
    return result

print(solution())