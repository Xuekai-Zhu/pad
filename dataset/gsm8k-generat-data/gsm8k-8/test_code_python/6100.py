def solution():
    # Calculate the number of grandchildren from each daughter
    daughters_grandchildren = 3 * 6

    # Calculate the number of grandchildren from each son
    sons_grandchildren = 3 * 5

    # Calculate the total number of grandchildren
    total_grandchildren = daughters_grandchildren + sons_grandchildren

    result = total_grandchildren
    return result

print(solution())