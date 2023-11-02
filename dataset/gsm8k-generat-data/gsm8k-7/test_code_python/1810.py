def solution():
    total_income = 80 + 60

    # Calculate the number of capsules of 100 mg amoxicillin sold
    num_capsules_100mg = 80 / 5

    # Calculate the number of capsules of 500 mg amoxicillin sold
    num_capsules_500mg = 60 / 2

    # Calculate the total number of capsules sold
    total_num_capsules = num_capsules_100mg + num_capsules_500mg

    # Calculate the number of capsules sold every 2 weeks
    num_capsules_2_weeks = total_num_capsules * 2
    result = num_capsules_2_weeks
    return result

print(solution())