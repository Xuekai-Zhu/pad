def solution():
    # Calculate the number of crayons Martha lost
    lost_crayons = 18 / 2

    # Calculate the number of crayons Martha has left
    remaining_crayons = 18 - lost_crayons

    # Add the new set of crayons
    total_crayons = remaining_crayons + 20
    result = total_crayons
    return result

print(solution())