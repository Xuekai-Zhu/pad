def solution():
    total_apples = 55  # Jack bought 55 apples
    father = 10  # Jack gives 10 apples to his father
    remaining_apples = total_apples - father  # Jack has remaining apples to share

    # Calculate the number of apples each person will get
    apples_per_person = remaining_apples // 5  # Jack has 4 friends, so there are 5 people in total

    result = apples_per_person
    return result

print(solution())