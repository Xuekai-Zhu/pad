def solution():
    brian_shoes = 22  # Brian has 22 pairs of shoes
    edward_shoes = 3 * brian_shoes  # Edward has 3 times the number of shoes Brian has
    jacob_shoes = edward_shoes / 2  # Jacob has half the number of shoes Edward has

    # Calculate the total number of shoes they have in pairs
    total_shoes = brian_shoes + edward_shoes + jacob_shoes
    result = total_shoes
    return result

print(solution())