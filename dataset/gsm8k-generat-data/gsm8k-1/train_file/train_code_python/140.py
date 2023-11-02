def solution():
    """Larry spends half an hour twice a day walking and playing with his dog. He also spends a fifth of an hour every day feeding his dog. How many minutes does Larry spend on his dog each day?"""
    walking_time = 0.5
    playing_time = 0.5
    feeding_time = 0.2
    total_time = (walking_time + playing_time + feeding_time) * 60
    result = total_time
    return result

print(solution())