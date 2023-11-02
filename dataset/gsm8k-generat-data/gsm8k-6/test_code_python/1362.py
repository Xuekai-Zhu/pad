def solution():
    # Calculate the total number of gumballs after purchasing more
    total_gumballs = (40 + 60) + 4*(40 + 60)

    # Divide the total number of gumballs equally between Joanna and Jacques
    each_gets = total_gumballs / 2
    result = each_gets
    return result

print(solution())