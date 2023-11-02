def solution():
    """Greg has his own dog walking business. He charges $20 per dog plus $1 per minute per dog for walking the dog. If he walks one dog for 10 minutes, two dogs for 7 minutes and three dogs for 9 minutes, how much money, in dollars, does he earn?"""
    dog_one_price = 20 + (10 * 1)
    dog_two_price = (20 * 2) + (7 * 2)
    dog_three_price = (20 * 3) + (9 * 3)
    total_earnings = dog_one_price + dog_two_price + dog_three_price
    result = total_earnings
    return result

print(solution())