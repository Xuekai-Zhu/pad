def solution():
    """Belinda’s dog is missing, so she made 200 flyers to distribute around town with the help of her friends. Ryan passed out 42 flyers, Alyssa passed out 67, Scott passed out 51 and Belinda passed out the rest. What percentage of the flyers did Belinda pass out?"""
    # Define the total number of flyers and the number of flyers distributed by Ryan, Alyssa, and Scott
    total_flyers = 200
    flyers_distributed = 42 + 67 + 51

    # Calculate the number of flyers distributed by Belinda
    belinda_flyers = total_flyers - flyers_distributed

    # Calculate the percentage of flyers distributed by Belinda
    belinda_percentage = (belinda_flyers / total_flyers) * 100

    # return the result
    result = belinda_percentage
    return result

print(solution())