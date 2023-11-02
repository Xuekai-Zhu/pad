def solution():
    """A bicycle store is running a promotion. Every time a customer buys a bicycle, they will receive 2 bike clamps free with it. If the store sells 19 bikes in the morning and 27 bikes in the afternoon, how many bike clamps has the store given to customers?"""
    bikes_sold_morning = 19
    bikes_sold_afternoon = 27
    clamps_per_bike = 2
    total_clamps = (bikes_sold_morning + bikes_sold_afternoon) * clamps_per_bike
    result = total_clamps
    return result

print(solution())