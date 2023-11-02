def solution():
    """A bicycle store is running a promotion. Every time a customer buys a bicycle, they will receive 2 bike clamps free with it. If the store sells 19 bikes in the morning and 27 bikes in the afternoon, how many bike clamps has the store given to customers?"""
    # Define the number of bikes sold in the morning and afternoon
    morning_bikes = 19
    afternoon_bikes = 27

    # Calculate the total number of bike clamps given to customers
    total_clamps = (morning_bikes + afternoon_bikes) * 2

    # Display the total number of bike clamps
    result = total_clamps
    return result

print(solution())