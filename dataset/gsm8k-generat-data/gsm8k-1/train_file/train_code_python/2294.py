def solution():
    """Chalktown High School had their prom last weekend. There were 123 students who attended. If 3 students attended on their own, how many couples came to the prom?"""
    total_students = 123
    students_on_their_own = 3
    couples = (total_students - students_on_their_own) / 2
    result = couples
    return result

print(solution())