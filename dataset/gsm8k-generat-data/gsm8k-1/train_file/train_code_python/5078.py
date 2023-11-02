def solution():
    """Connor is taking his date to the movies. The tickets cost $10.00 each. They decided to get the large popcorn & 2 drink combo meal for $11.00 and each grab a box of candy for $2.50 each. How much will Connor spend on his date?"""
    ticket_cost = 10
    popcorn_drink_cost = 11
    candy_cost = 2.5
    num_candies = 2
    total_cost = (ticket_cost * 2) + popcorn_drink_cost + (candy_cost * num_candies)
    result = total_cost
    return result

print(solution())