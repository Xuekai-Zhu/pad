def solution():
    """A class of 12 students was about to share 108 oranges equally among themselves when it was discovered that 36 of the oranges were bad and had to be thrown away. How many oranges less will each student get now than if no orange had to be thrown away?"""
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