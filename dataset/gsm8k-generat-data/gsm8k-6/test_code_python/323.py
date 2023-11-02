def solution():
    # Find the total number of flags needed
    total_flags = 22 + 36 + 2  # Jay invited 22 people and Gloria invited 36, plus they wanted one each

    # Find the number of packs of flags needed
    packs_of_flags = total_flags // 5  # 5 flags for $1.00, round down

    # Find the total cost of the flags
    total_cost = packs_of_flags * 1.00  # 1 pack of 5 flags costs $1.00

    result = total_cost
    return result

print(solution())