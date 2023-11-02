def solution():
    # Let x be the number of employees hired in the third week
    x = (400/2)/2

    # Calculate the number of employees hired in each week based on the given information
    week1 = x + 200
    week2 = x + 50
    week3 = x
    week4 = 400

    # Calculate the total number of employees hired in a month
    total_employees = week1 + week2 + week3 + week4

    # Calculate the average number of employees hired per week
    average_employees = total_employees / 4
    result = average_employees
    return result

print(solution())