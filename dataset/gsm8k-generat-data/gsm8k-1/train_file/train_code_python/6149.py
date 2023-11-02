def solution():
    """Manny has a tree that grows at the rate of fifty centimeters every two weeks. If the tree is currently 2 meters tall, how tall, in centimeters, will the tree be in 4 months?"""
    current_height = 2  # meters
    growth_rate = 50  # centimeters every two weeks
    weeks_in_four_months = 16  # 4 months = 16 weeks
    additional_height = (growth_rate / 2) * weeks_in_four_months
    total_height_cm = (current_height * 100) + additional_height  # convert to cm
    result = total_height_cm
    
    return result

print(solution())