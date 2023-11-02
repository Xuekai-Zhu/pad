def solution():
    
    total_oranges = 108
    bad_oranges = 36
    good_oranges = total_oranges - bad_oranges
    num_students = 12
    original_share = total_oranges // num_students
    new_share = good_oranges // num_students
    difference = original_share - new_share
    result = difference
    return result

print(solution())