def solution():
    # Calculate the number of houses that can be painted in 3 hours
    minutes_in_3_hours = 60 * 3  # convert 3 hours to minutes
    houses_painted = minutes_in_3_hours // 20  # integer division to get whole number of houses painted
    result = houses_painted
    return result

print(solution())