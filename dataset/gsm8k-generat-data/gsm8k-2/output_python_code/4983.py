def solution():
    """Bill and Joan both work for a library. 5 years ago, Joan had 3 times as much experience as Bill. Now she has twice as much experience as Bill. How many years of experience does Bill have now?"""
    years_ago = 5
    joan_multiplier = 3
    current_multiplier = 2
    difference_in_multiplier = current_multiplier - joan_multiplier
    bill_years = years_ago * difference_in_multiplier
    joan_years = joan_multiplier * bill_years
    total_years = bill_years + joan_years
    result = total_years
    return result

print(solution())