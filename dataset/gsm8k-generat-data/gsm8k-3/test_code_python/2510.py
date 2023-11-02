def solution():
    """Lindsey saved $50 in September, she saved $37 in October, and $11 in November. Lindsey's mom said that since Lindsey had saved more than $75,  she would give Lindsey $25.  Then Lindsey spent $87 on a video game. How much money did Lindsey have left?"""
    # Calculate the total amount saved
    total_saved = 50 + 37 + 11

    # Check if Lindsey saved more than $75
    if total_saved > 75:
        # If she did, add $25 from her mom
        total_saved += 25

    # Subtract the cost of the video game
    remaining_money = total_saved - 87

    # Display the remaining money
    result = remaining_money
    return result

print(solution())