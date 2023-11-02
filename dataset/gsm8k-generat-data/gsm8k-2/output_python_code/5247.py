def solution():
    """John used to be able to squat 135 pounds. After training, he increased that by 265 pounds. He then gets a magical strength-increasing bracer that increases his strength by an additional 600%. How much can he now lift?"""
    base_squat = 135
    training_increase = 265
    total_weight = base_squat + training_increase
    bracer_increase = total_weight * 6
    final_weight = total_weight + bracer_increase
    result = final_weight
    return result

print(solution())