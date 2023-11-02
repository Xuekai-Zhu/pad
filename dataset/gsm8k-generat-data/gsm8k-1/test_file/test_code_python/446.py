def solution():
    """You can buy a movie super ticket for $20 that includes rights to watch any movie and you get one popcorn with a soda for only $1 extra. Or you can buy a movie ticket for $12 and buy one popcorn and a soda at regular price. What's the regular price of popcorn if the soda costs $3 and you didn't buy the super ticket and ended up saving $2?"""
    super_ticket_price = 20
    popcorn_price = None
    soda_price = 3
    regular_ticket_price = 12
    total_regular_price = regular_ticket_price + soda_price

    # Find the price of the popcorn
    for i in range(1, 10):
        total_super_price = super_ticket_price + i
        if total_regular_price + i == total_super_price - 2:
            popcorn_price = i
            break

    result = popcorn_price
    return result

print(solution())