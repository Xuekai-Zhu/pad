def solution():
    monday_donuts = 14
    tuesday_donuts = monday_donuts / 2
    wednesday_donuts = monday_donuts * 4

    # Calculate the total number of donuts Andrew ate
    total_donuts = monday_donuts + tuesday_donuts + wednesday_donuts
    result = total_donuts
    return result

print(solution())