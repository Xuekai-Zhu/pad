def solution():
    """After a trip, Mrs. Nalani took the students to the restaurant and told them they could order either a burger or a hot dog.
    If the number of students who ordered burgers was 30, twice the number of students who called for a hot dog,
    calculate the number of students at the restaurant."""
    
    # Let the number of students who ordered hot dogs be x
    x = 15
    
    # The number of students who ordered burgers is 30
    # And twice the number of students who ordered hot dogs is 2x
    # Therefore, the total number of students is:
    total_students = 30 + x + 2*x
    
    # Return the result
    return total_students

print(solution())