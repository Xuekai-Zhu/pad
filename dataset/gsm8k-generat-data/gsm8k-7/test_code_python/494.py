def solution():
    small_house = 5200
    big_house = 7300
    total = 16000

    # Calculate the current total square footage before expansion
    current_total = small_house + big_house

    # Calculate the amount the small house needs to be expanded by
    expansion = total - current_total

    result = expansion
    return result

print(solution())