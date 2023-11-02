def solution():
    """Chalktown High School had their prom last weekend. There were 123 students who attended. If 3 students attended on their own, how many couples came to the prom?"""
    # Define the number of solo attendees
    solo_attendees = 3

    # Calculate the number of couples
    couples = (123 - solo_attendees) / 2

    # Return the result
    result = couples
    return result

print(solution())