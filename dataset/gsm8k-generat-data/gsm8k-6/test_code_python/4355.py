def solution():
    # Calculate the number of people at the game on Monday
    monday = 80 - 20

    # Calculate the number of people at the game on Wednesday
    wednesday = monday + 50

    # Calculate the number of people at the game on Friday
    friday = 80 + monday

    # Calculate the total number of people who attended the games during the week
    total_attendance = monday + wednesday + friday + 80

    # Calculate the difference between the expected total audience and the actual total attendance
    difference = total_attendance - 350

    result = difference
    return result

print(solution())