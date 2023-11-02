def solution():
    total_spent = 80
    num_20s = 0
    num_10s = 0

    # Find number of 20s and 10s used to pay
    while total_spent > 0:
        if total_spent >= 20:
            total_spent -= 20
            num_20s += 1
        elif total_spent >= 10:
            total_spent -= 10
            num_10s += 1
    # Calculate number of $10 bills given
    num_10s_given = num_20s - 1
    result = num_10s_given
    return result

print(solution())