def solution():
    """Chris wanted to buy a new video game that costs $60 as well as an assortment of candy that costs $5. To earn the money, he agreed to babysit his little sister for $8 per hour. If he works 9 hours, how much money will be left over after he makes his purchases?"""
    video_game_cost = 60
    candy_cost = 5
    hours_worked = 9
    hourly_rate = 8
    money_earned = hourly_rate * hours_worked
    total_cost = video_game_cost + candy_cost
    money_left_over = money_earned - total_cost
    result = money_left_over
    return result

print(solution())