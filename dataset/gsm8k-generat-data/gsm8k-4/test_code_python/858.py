def solution():
    """It is recommended that men should consume no more than 150 calories of added sugar per day. Mark took a soft drink in the afternoon that contained 2500 calories, 5% of which was from added sugar. Then he bought some bars of candy which had 25 calories of added sugar each. If he eventually exceeded the recommended intake of added sugar by 100%, how many bars of candy did he take?"""
    # Define the daily recommended intake of added sugar
    RECOMMENDED_INTAKE = 150

    # Calculate the amount of added sugar in the soft drink
    soft_drink_sugar = 2500 * 0.05

    # Calculate the remaining amount of added sugar that Mark can consume
    remaining_sugar = RECOMMENDED_INTAKE - soft_drink_sugar

    # Calculate the number of bars of candy that Mark can consume
    candy_bars = remaining_sugar / 25

    # Calculate the number of candy bars that Mark actually consumed
    actual_candy_bars = candy_bars * 2

    # Return the result
    result = actual_candy_bars
    return result

print(solution())