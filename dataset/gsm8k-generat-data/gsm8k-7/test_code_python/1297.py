def solution():
    num_students = 40
    pct_with_puppies = 0.8
    pct_with_puppies_and_parrots = 0.25

    # Calculate the number of students with puppies
    num_with_puppies = num_students * pct_with_puppies

    # Calculate the number of students with both puppies and parrots
    num_with_both = num_with_puppies * pct_with_puppies_and_parrots

    result = num_with_both
    return result

print(solution())