def solution():
    # Calculate the total number of apples Billy ate during the week

    monday = 2
    tuesday = 2 * monday
    friday = monday / 2
    thursday = 4 * friday

    total_apples = monday + tuesday + friday + thursday + 0  # not sure what he ate on Wednesday

    # Calculate the number of apples Billy ate on Wednesday
    wednesday = 20 - total_apples

    result = wednesday
    return result

print(solution())