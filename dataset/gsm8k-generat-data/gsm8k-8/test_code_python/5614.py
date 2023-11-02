def solution():
    # Calculate the total revenue from walking the 20 dogs
    total_revenue = (20 * 2) + (20 * 1.25 * 10)

    # Calculate the amount each family member has to contribute for the vacation
    vacation_cost = 1000
    num_family_members = 5
    individual_cost = vacation_cost / num_family_members

    # Calculate the number of blocks Jules has to walk the dogs to cover the vacation cost
    blocks_needed = (individual_cost - total_revenue) / (1.25 * 20)
    result = blocks_needed
    return result

print(solution())