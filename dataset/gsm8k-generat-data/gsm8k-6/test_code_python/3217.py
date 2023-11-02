def solution():
    # Calculate the number of pens bought by each friend
    robert_pens = 4
    julia_pens = 3 * robert_pens
    dorothy_pens = julia_pens / 2

    # Calculate the total cost of pens bought by the friends
    total_pens_cost = (robert_pens + julia_pens + dorothy_pens) * 1.5  # assuming one pen costs $1.50

    result = total_pens_cost
    return result

print(solution())