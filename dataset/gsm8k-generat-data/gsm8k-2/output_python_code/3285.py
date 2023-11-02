def solution():
    """John decides to get a new phone number and it ends up being a recycled number. He used to get 20 text messages a day. Now he is getting 55. Assuming the number of texts his friends send has not changed, how many text messages per week is he getting that are not intended for him?"""
    daily_unintended = 55 - 20
    weekly_unintended = daily_unintended * 7
    result = weekly_unintended
    return result

print(solution())