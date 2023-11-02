def solution():
    # Calculate the number of students with brown eyes and black hair
    brown_eyes = 6  # given
    brown_black = brown_eyes / 0.5  # half of the students with brown eyes have black hair

    # Calculate the total number of students in the class
    total = brown_black / (2/3)  # two-thirds of the class have brown eyes

    result = total
    return result

print(solution())