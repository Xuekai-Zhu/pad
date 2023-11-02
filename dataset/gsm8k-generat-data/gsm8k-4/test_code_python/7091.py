def solution():
    """A bicycle store is running a promotion. Every time a customer buys a bicycle, they will receive 2 bike clamps free with it. If the store sells 19 bikes in the morning and 27 bikes in the afternoon, how many bike clamps has the store given to customers?"""
    # Define the number of bikes sold in the morning and afternoon
    bikes_morning = 19
    bikes_afternoon = 27

    # Calculate the total number of bikes sold
    total_bikes = bikes_morning + bikes_afternoon

    # Calculate the total number of bike clamps given away
    total_clamps = total_bikes * 2

    # return the result
    result = total_clamps
    return result

print(solution())