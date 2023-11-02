def solution():
    # Calculate the number of sandwiches needed for all the students
    sandwiches = 2 * 6 * 5  # each group has 6 students (5+1), and each student needs 2 sandwiches
    # Calculate the number of bread slices needed for all the sandwiches
    bread_slices = sandwiches * 2  # each sandwich has 2 bread slices
    result = bread_slices
    return result

print(solution())