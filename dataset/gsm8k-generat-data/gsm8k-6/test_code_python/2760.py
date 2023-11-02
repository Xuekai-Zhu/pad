def solution():
    dad_age = 32
    joel_age = 5
    difference = dad_age - joel_age  # Find the age difference between Joel and his dad
    double_age_difference = difference * 2  # Find the age when dad is twice as old as Joel
    future_joel_age = double_age_difference + joel_age  # Add the age difference to Joel's current age
    result = future_joel_age
    return result

print(solution())