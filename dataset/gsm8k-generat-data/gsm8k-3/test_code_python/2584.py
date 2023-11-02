def solution():
    """Belinda’s dog is missing, so she made 200 flyers to distribute around town with the help of her friends. Ryan passed out 42 flyers, Alyssa passed out 67, Scott passed out 51 and Belinda passed out the rest. What percentage of the flyers did Belinda pass out?"""
    # Define the number of flyers distributed by each person
    ryan_flyers = 42
    alyssa_flyers = 67
    scott_flyers = 51

    # Calculate the total number of flyers distributed by all four people
    total_flyers = ryan_flyers + alyssa_flyers + scott_flyers

    # Calculate the number of flyers distributed by Belinda
    belinda_flyers = 200 - total_flyers

    # Calculate the percentage of flyers distributed by Belinda
    belinda_percentage = (belinda_flyers / 200) * 100

    # Display the percentage of flyers distributed by Belinda
    result = belinda_percentage
    return result

print(solution())