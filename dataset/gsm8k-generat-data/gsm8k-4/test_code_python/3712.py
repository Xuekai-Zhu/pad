def solution():
    """Peter is raking leaves. It takes him 15 minutes to rake 3 bags of leaves. If he keeps raking at the same rate, how long will it take him to rake 8 bags?"""
    
    # Calculate the time it takes to rake one bag of leaves
    time_per_bag = 15/3
    
    # Calculate the total time it will take to rake 8 bags of leaves
    total_time = time_per_bag * 8
    
    result = total_time
    return result

print(solution())