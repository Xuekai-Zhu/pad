def solution():
    # Calculate the total number of people drawing
    total_people = 4+3  # Erika and her 3 siblings plus 3 friends

    # Calculate the total number of chalk originally available
    total_chalk = total_people * 3 - 2 + 12  # everyone should have 3 pieces of chalk each minus 2 lost pieces plus 12 more pieces brought by Erika's mom

    # Calculate the number of chalk Erika and her siblings originally had
    siblings_chalk = total_chalk - 3*4  # subtract the 3 pieces each that Erika and her 3 siblings have now
    result = siblings_chalk
    return result

print(solution())