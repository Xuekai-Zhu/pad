def solution():
    """After a trip, Mrs. Nalani took the students to the restaurant and told them they could order either a burger or a hot dog. If the number of students who ordered burgers was 30, twice the number of students who called for a hot dog, calculate the number of students at the restaurant."""
    burger_count = 30
    hotdog_count = burger_count // 2
    total_students = burger_count + hotdog_count
    result = total_students
    return result

print(solution())