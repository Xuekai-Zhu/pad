def solution():
    """Bert bought some unique stamps for his collection. Before the purchase, he had only half the stamps he bought. If he bought 300 stamps, how many stamps does Bert have in total after the purchase?"""
    bought_stamps = 300
    initial_stamps = bought_stamps / 2
    total_stamps = initial_stamps + bought_stamps
    result = total_stamps
    return result

print(solution())