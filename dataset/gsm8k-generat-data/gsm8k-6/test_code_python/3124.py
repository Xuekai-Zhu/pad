def solution():
    # Find the number of clothes Nicole's first sister had
    first_sister_clothes = 10 / 2

    # Find the number of clothes Nicole's second sister had
    second_sister_clothes = 10 + 2

    # Find the average number of clothes Nicole's younger sisters had (excluding Nicole)
    average_younger_sisters_clothes = (first_sister_clothes + second_sister_clothes + 10) / 3

    # Find the total number of clothes Nicole ends up with
    total_clothes = 10 + first_sister_clothes + second_sister_clothes + average_younger_sisters_clothes

    result = total_clothes
    return result

print(solution())