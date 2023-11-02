def solution():
    """There are six chairs in each row in a church. If there are 20 rows of chairs in the church, and each chair holds five people, calculate the number of people who have to sit in the chairs for the church to be full."""
    chairs_per_row = 6
    rows_of_chairs = 20
    people_per_chair = 5
    total_chairs = chairs_per_row * rows_of_chairs
    total_people = total_chairs * people_per_chair
    result = total_people
    return result

print(solution())