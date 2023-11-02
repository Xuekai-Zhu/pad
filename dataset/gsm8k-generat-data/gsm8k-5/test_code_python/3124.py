def solution():
    # Calculate how many pieces of clothing Nicole's first sister had
    sister_one_clothes = 10 / 2

    # Calculate how many pieces of clothing Nicole's second sister had
    sister_two_clothes = 10 + 2

    # Calculate the average number of pieces of clothing of Nicole and her three sisters
    total_clothes = 10 + sister_one_clothes + sister_two_clothes
    average_clothes = total_clothes / 4

    # Nicole ends up with the average number of pieces of clothing
    result = average_clothes
    return result

print(solution())