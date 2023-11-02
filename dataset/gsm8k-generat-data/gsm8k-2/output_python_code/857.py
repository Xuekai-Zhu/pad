def solution():
    """It is recommended that men should consume no more than 150 calories of added sugar per day. Mark took a soft drink in the afternoon that contained 2500 calories, 5% of which was from added sugar. Then he bought some bars of candy which had 25 calories of added sugar each. If he eventually exceeded the recommended intake of added sugar by 100%, how many bars of candy did he take?"""
    soft_drink_calories = 2500
    added_sugar_soft_drink = 0.05 * soft_drink_calories
    candy_calories = 25
    max_added_sugar = 150
    max_candy = (max_added_sugar - added_sugar_soft_drink) / candy_calories
    excess_candy = max_candy
    total_candy = excess_candy * 2  # 100% over the recommended intake
    result = total_candy
    return result

print(solution())