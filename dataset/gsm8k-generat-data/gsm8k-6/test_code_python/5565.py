def solution():
    # Calculate the number of students enrolled in Statistics
    enrolled_statistics = 120 / 2  # half of the students are enrolled in Statistics

    # Calculate the number of seniors enrolled in Statistics
    seniors_in_statistics = 0.9 * enrolled_statistics  # 90 percent of students in Statistics are seniors

    result = seniors_in_statistics
    return result

print(solution())