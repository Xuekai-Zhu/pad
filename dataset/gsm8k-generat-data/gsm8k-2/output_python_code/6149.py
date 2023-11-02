def solution():
    """Manny has a tree that grows at the rate of fifty centimeters every two weeks. If the tree is currently 2 meters tall, how tall, in centimeters, will the tree be in 4 months?"""
    initial_height = 200  # in centimeters
    growth_rate = 50  # in centimeters every 2 weeks
    time_in_weeks = 4 * 4  # 4 months is 16 weeks
    additional_height = (growth_rate / 2) * (time_in_weeks // 2)
    total_height = initial_height + additional_height
    result = total_height
    return result

print(solution())