def solution():
    """It is recommended that men should consume no more than 150 calories of added sugar per day. Mark took a soft drink in the afternoon that contained 2500 calories, 5% of which was from added sugar. Then he bought some bars of candy which had 25 calories of added sugar each. If he eventually exceeded the recommended intake of added sugar by 100%, how many bars of candy did he take?"""
    max_added_sugar = 150
    soft_drink_calories = 2500
    soft_drink_added_sugar = soft_drink_calories * 0.05
    candy_added_sugar = max_added_sugar * 2 - soft_drink_added_sugar
    bars_of_candy = candy_added_sugar / 25
    result = bars_of_candy
    return result

print(solution())