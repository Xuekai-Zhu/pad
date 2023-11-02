def solution():
    # Calculate the remaining length of the fence after each friend whitewashed their portion
    remaining_length = 100 - 10  # Ben whitewashed 10 feet
    remaining_length = remaining_length - (remaining_length / 5)  # Billy whitewashed a fifth of the remaining fence
    remaining_length = remaining_length - (remaining_length / 3)  # Johnny whitewashed a third of the remaining fence

    result = remaining_length
    return result

print(solution())