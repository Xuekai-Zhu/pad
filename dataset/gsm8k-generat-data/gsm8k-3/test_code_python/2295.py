def solution():
    """Chalktown High School had their prom last weekend. There were 123 students who attended. If 3 students attended on their own, how many couples came to the prom?"""
    # Define the total number of students who attended the prom
    total_students = 123

    # Define the number of students who attended on their own
    solo_students = 3

    # Calculate the number of couples who attended the prom
    couples = (total_students - solo_students) / 2

    # Display the number of couples
    result = couples
    return result

print(solution())