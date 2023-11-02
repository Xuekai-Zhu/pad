def solution():
    # Calculate the total number of cans Collin has
    cans_at_home = 12
    cans_at_grandparents = 3 * cans_at_home
    cans_from_neighbor = 46
    cans_from_dad = 250
    total_cans = cans_at_home + cans_at_grandparents + cans_from_neighbor + cans_from_dad

    # Calculate Collin's earnings from the cans
    earnings = 0.25 * total_cans

    # Calculate the amount to be put into savings
    savings = earnings / 2
    result = savings
    return result

print(solution())