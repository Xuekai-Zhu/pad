def solution():
    # Calculate the total number of students after merging classes
    total_students = 10 + 10  # two classes with the same amount of students

    # Calculate the total number of adults at the zoo
    total_adults = 5 + 2  # 5 parents and 2 teachers

    # Calculate the number of individuals that left the zoo
    individuals_left = 10 + 2  # 10 students and 2 chaperone parents

    # Calculate the number of individuals left at the zoo
    individuals_at_zoo = total_students + total_adults - individuals_left
    result = individuals_at_zoo
    return result

print(solution())