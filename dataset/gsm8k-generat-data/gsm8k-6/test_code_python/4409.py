def solution():
    # Calculate the total number of tins of beans in the delivery
    total_tins = 15 * 24

    # Calculate the number of damaged tins
    damaged_tins = 0.05 * total_tins

    # Calculate the number of tins left after throwing away the damaged ones
    remaining_tins = total_tins - damaged_tins
    result = remaining_tins
    return result

print(solution())