def solution():
    """Sidney does 20 jumping jacks on Monday, 36 on Tuesday, 40 on Wednesday, and 50 on Thursday. Brooke does three times as many jumping jacks as Sidney. How many jumping jacks did Brooke do?"""
    # Calculate the total number of jumping jacks that Sidney did in the week
    sidney_total = 20 + 36 + 40 + 50

    # Calculate the number of jumping jacks that Brooke did (three times as many as Sidney)
    brooke_total = sidney_total * 3

    result = brooke_total
    return result

print(solution())