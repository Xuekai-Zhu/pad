def solution():
    """The chances of making the junior high basketball team start at 10% if you're 66 inches and increase 10% for every additional inch of height. Devin starts out as 65 inches tall, then grows 3 inches. What are his chances of making the basketball team?"""
    # Define the base chance and increase per inch
    BASE_CHANCE = 0.1
    INCREASE_PER_INCH = 0.1

    # Define Devin's height before and after growth
    height_before = 65
    height_after = height_before + 3

    # Calculate Devin's chance of making the team before and after growth
    chance_before = BASE_CHANCE + (height_before - 66) * INCREASE_PER_INCH
    chance_after = BASE_CHANCE + (height_after - 66) * INCREASE_PER_INCH

    # Display Devin's chances before and after growth
    result = chance_after
    return result

print(solution())