def solution():
    """The chances of making the junior high basketball team start at 10% if you're 66 inches and increase 10% for every additional inch of height. Devin starts out as 65 inches tall, then grows 3 inches. What are his chances of making the basketball team?"""
    base_chance = 10
    base_height = 66
    height_increase = 10
    devin_height = 65 + 3
    height_difference = devin_height - base_height
    chance_increase = (height_difference * height_increase)
    final_chance = base_chance + chance_increase
    result = final_chance
    return result

print(solution())