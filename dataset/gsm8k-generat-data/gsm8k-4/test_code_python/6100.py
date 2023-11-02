def solution():
    """Grandma Olga has 3 daughters and 3 sons. If all her daughters each have 6 sons, and each of her sons has 5 daughters, how many grandchildren does she have in total?"""
    # Calculate the number of grandchildren from daughters
    daughters_grandchildren = 3 * 6 * 2

    # Calculate the number of grandchildren from sons
    sons_grandchildren = 3 * 5 * 3

    # Calculate the total number of grandchildren
    total_grandchildren = daughters_grandchildren + sons_grandchildren

    result = total_grandchildren
    return result

print(solution())