def solution():
    # Calculate the total number of portions from 20 sandwiches cut in half twice
    total_portions = 20 * 2 * 2

    # Calculate the number of people that can be fed with 8 portions each
    num_people = total_portions // 8

    result = num_people
    return result

print(solution())