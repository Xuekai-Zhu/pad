def solution():
    first_protest_days = 4
    second_protest_days = first_protest_days * 1.25  # 25% longer than the first protest

    total_days_protesting = first_protest_days + second_protest_days
    result = total_days_protesting
    return result

print(solution())