def solution():
    total_apples = 20
    monday_apples = 2
    thursday_apples = 0  # initialize to zero
    friday_apples = 0  # initialize to zero

    # Calculate the number of apples Billy ate on Tuesday
    tuesday_apples = monday_apples * 2

    # Calculate the number of apples Billy ate on Friday
    friday_apples = monday_apples / 2

    # Calculate the number of apples Billy ate on Thursday based on what he ate on Friday
    thursday_apples = friday_apples * 4

    # Calculate the total number of apples Billy ate excluding Wednesday
    total_excluding_wednesday = monday_apples + tuesday_apples + thursday_apples + friday_apples

    # Calculate the number of apples Billy ate on Wednesday
    wednesday_apples = total_apples - total_excluding_wednesday
    result = wednesday_apples
    return result

print(solution())