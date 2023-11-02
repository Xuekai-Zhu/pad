def solution():
    """It is recommended that men should consume no more than 150 calories of added sugar per day. Mark took a soft drink in the afternoon that contained 2500 calories, 5% of which was from added sugar. Then he bought some bars of candy which had 25 calories of added sugar each. If he eventually exceeded the recommended intake of added sugar by 100%, how many bars of candy did he take?"""
    # Define the recommended daily intake of added sugar
    DAILY_LIMIT = 150

    # Calculate the added sugar in the soft drink
    soft_drink_sugar = 0.05 * 2500

    # Calculate the added sugar from the candy bars
    candy_sugar = (DAILY_LIMIT + soft_drink_sugar) * 2 - soft_drink_sugar
    candy_bars = candy_sugar / 25

    # Display the number of candy bars Mark took
    result = candy_bars
    return result

print(solution())