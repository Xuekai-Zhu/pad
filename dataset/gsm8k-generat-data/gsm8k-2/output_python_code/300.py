def solution():
    """240 sixth-grade students were asked about the number of novels they read per month. 1/6 of students read three or more novels, 35% of students read two novels, 5/12 of students read one novel, and the rest of the students do not read anything. Calculate the number of students who do not read novels."""
    total_students = 240
    three_or_more = total_students * (1/6)
    two = total_students * 0.35
    one = total_students * (5/12)
    no_read = total_students - (three_or_more + two + one)
    result = no_read
    return result

print(solution())