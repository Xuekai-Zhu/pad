def solution():
    total_students = 100  # We know that 60% of the students are girls, so 40% must be boys
    boys_percent = 40
    boys = 300  # We are given that there are 300 boys at the school

    # Calculate the total number of students at the school
    total = (boys * 100) / boys_percent

    # Calculate the number of girls at the school
    girls = total - boys

    result = girls
    return result

print(solution())