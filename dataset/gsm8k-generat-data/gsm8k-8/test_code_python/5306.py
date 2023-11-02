def solution():
    # Calculate the number of adults at the reunion
    adult_count = 45 * 3

    # Calculate the number of adults who wore blue
    blue_count = adult_count // 3

    # Calculate the number of adults who did not wear blue
    not_blue_count = adult_count - blue_count

    result = not_blue_count
    return result

print(solution())