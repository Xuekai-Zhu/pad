def solution():
    total_apples = 20  # Billy ate 20 apples this week
    monday_apples = 2  # Billy ate 2 apples on Monday

    # Calculate the number of apples Billy ate on Tuesday
    tuesday_apples = monday_apples * 2

    # Calculate the number of apples Billy ate on Friday
    friday_apples = monday_apples / 2

    # Calculate the number of apples Billy ate on Thursday
    thursday_apples = friday_apples * 4

    # Calculate the number of apples Billy ate on Wednesday
    wednesday_apples = total_apples - monday_apples - tuesday_apples - thursday_apples
    result = wednesday_apples
    return result

print(solution())