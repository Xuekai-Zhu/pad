def solution():
    # Calculate the total time Mr. Willson worked from Monday to Friday
    monday_time = 3/4  # hours worked on Monday
    tuesday_time = 1/2  # hours worked on Tuesday
    wednesday_time = 2/3  # hours worked on Wednesday
    thursday_time = 5/6  # hours worked on Thursday
    friday_time = 75/60  # hours worked on Friday (converted from minutes to hours)
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time + friday_time
    result = total_time
    return result

print(solution())