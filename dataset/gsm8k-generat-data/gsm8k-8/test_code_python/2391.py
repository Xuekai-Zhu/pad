def solution():
    # Calculate the total number of chocolate candy pieces made last Monday
    last_monday_candy = 40

    # Calculate the number of students Lucas has
    total_students = last_monday_candy // 4

    # Calculate the number of candy pieces he will make for the remaining students
    remaining_students = total_students - 3
    candy_for_remaining_students = remaining_students * 4

    result = candy_for_remaining_students
    return result

print(solution())