def solution():
    """The chances of making the junior high basketball team start at 10% if you're 66 inches and increase 10% for every additional inch of height. Devin starts out as 65 inches tall, then grows 3 inches. What are his chances of making the basketball team?"""
    initial_height = 66
    initial_chance = 0.10
    extra_chance_per_inch = 0.10
    devin_height = 65 + 3
    devin_chance = initial_chance + (devin_height - initial_height) * extra_chance_per_inch
    result = devin_chance
    return result

print(solution())