def solution():
    """After a trip, Mrs. Nalani took the students to the restaurant and told them they could order either a burger or a hot dog. If the number of students who ordered burgers was 30, twice the number of students who called for a hot dog, calculate the number of students at the restaurant."""
    # Define the number of students who ordered burgers
    burger_students = 30

    # Calculate the number of students who ordered hot dogs
    hotdog_students = burger_students / 2

    # Calculate the total number of students at the restaurant
    total_students = burger_students + hotdog_students

    result = total_students
    return result

print(solution())