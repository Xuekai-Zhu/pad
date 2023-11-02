def solution():
    """Twice Betty's age is the cost of a pack of nuts. Doug, Betty's friend, is 40 years old. If the sum of their ages is 90, and Betty wants to buy 20 packs of the nuts, calculate the amount of money she'll pay for the packs of nuts."""
    # Doug is 40 years old
    doug_age = 40

    # Calculate Betty's age from the sum of their ages
    betty_age = 90 - doug_age

    # Calculate the cost per pack of nuts
    cost_per_pack = betty_age * 2

    # Calculate the total cost for 20 packs of nuts
    total_cost = cost_per_pack * 20

    # Display the total cost
    result = total_cost
    return result

print(solution())