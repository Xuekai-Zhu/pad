def solution():
    # Calculate the total number of balls in all 5 baskets
    total_balls = (15+5) * 5  # 15 tennis balls and 5 soccer balls in each of the 5 baskets

    # Calculate the total number of balls removed by the first 3 students
    removed_by_3_students = 8 * 3  

    # Calculate the total number of balls remaining after the first 3 students' turn
    total_remaining_balls = total_balls - removed_by_3_students  

    # Calculate the number of balls removed by the other 2 students
    removed_by_other_students = (total_remaining_balls - 56) / 2   

    result = removed_by_other_students
    return result

print(solution())