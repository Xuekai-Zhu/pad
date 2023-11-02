def solution():
    """For every 5 people that attend a poetry class, the teacher gives one of the students a lollipop. If 45 people show up for class, then another 15 come in a while later, how many lollipops did the teacher give away?"""
    total_people = 45 + 15
    lollipops_given = total_people // 5
    result = lollipops_given
    return result

print(solution())