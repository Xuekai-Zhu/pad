def solution():
    """At the beginning of an academic year, there were 15 boys in a class and the number of girls was 20% greater. Later in the year, transfer students were admitted such that the number of girls doubled but the number of boys remained the same. How many students are in the class now?"""
    
    # Calculate the number of girls at the beginning of the year
    girls_initial = int(15 * 1.2)

    # Calculate the total number of students at the beginning of the year
    total_initial = 15 + girls_initial

    # Calculate the number of girls after the transfer
    girls_after_transfer = girls_initial * 2

    # Calculate the total number of students after the transfer
    total_after_transfer = 15 + girls_after_transfer

    # Display the total number of students
    result = total_after_transfer
    return result

print(solution())