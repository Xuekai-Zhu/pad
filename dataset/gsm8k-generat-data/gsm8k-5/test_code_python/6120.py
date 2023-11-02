def solution():
    total_students = 200
    blue_likers = 0.3 * total_students  # 30% of the students like blue
    non_blue_likers = total_students - blue_likers
    red_likers = 0.4 * non_blue_likers  # 40% of non-blue likers like red
    yellow_likers = non_blue_likers - red_likers  # The rest like yellow

    # Calculate the combined number of students who like yellow and blue
    combined_likers = blue_likers + yellow_likers
    result = combined_likers
    return result

print(solution())