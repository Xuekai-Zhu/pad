def solution():
    """Lindsey saved $50 in September, she saved $37 in October, and $11 in November. Lindsey's mom said that since Lindsey had saved more than $75, she would give Lindsey $25. Then Lindsey spent $87 on a video game. How much money did Lindsey have left?"""
    # Calculate the total amount saved
    total_saved = 50 + 37 + 11

    # Check if Lindsey saved more than $75 to receive $25 from her mom
    if total_saved > 75:
        total_saved += 25

    # Calculate the amount remaining after purchasing the video game
    remaining_money = total_saved - 87

    # Return the result
    result = remaining_money
    return result

print(solution())