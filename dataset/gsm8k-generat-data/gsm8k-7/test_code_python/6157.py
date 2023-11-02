def solution():
    num_performances = 100
    num_disappearances = num_performances

    # Calculate the number of disappearances where the person never reappears
    num_never_reappear = num_disappearances // 10

    # Calculate the number of disappearances where two people reappear
    num_two_reappear = num_disappearances // 5

    # Calculate the total number of people who reappeared
    num_reappeared = (num_disappearances - num_never_reappear) + (num_two_reappear * 2)

    result = num_reappeared
    return result

print(solution())