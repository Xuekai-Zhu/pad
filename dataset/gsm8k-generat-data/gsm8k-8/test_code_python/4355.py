def solution():
    # Calculate the number of people on Monday
    monday = 80 - 20

    # Calculate the number of people on Wednesday
    wednesday = monday + 50

    # Calculate the number of people on Friday
    friday = 80 + monday

    # Calculate the total number of people for the week
    total = monday + wednesday + friday + 80

    # Calculate the difference between the expected total and actual total
    difference = total - 350
    result = difference
    return result

print(solution())