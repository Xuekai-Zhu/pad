def solution():
    """Julie wants to give her favorite cousin a $2345 mountain bike for his birthday. So far, she has saved $1500. Since the birthday is still a few weeks away, Julie has time to save even more. She plans on mowing 20 lawns, delivering 600 newspapers, and walking 24 of her neighbors’ dogs. She is paid $20 for each lawn, 40 cents per newspaper, and $15 per dog. After purchasing the bike, how much money will Julie have left?"""
    bike_cost = 2345
    saved_money = 1500
    lawns_mowed = 20
    newspapers_delivered = 600
    dogs_walked = 24
    lawn_payment = 20
    newspaper_payment = 0.4
    dog_payment = 15
    total_earned = lawns_mowed * lawn_payment + newspapers_delivered * newspaper_payment + dogs_walked * dog_payment
    total_money = saved_money + total_earned
    money_left = total_money - bike_cost
    result = money_left
    return result

print(solution())