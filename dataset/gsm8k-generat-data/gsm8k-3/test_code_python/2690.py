def solution():
    """Bonnie and Samuel went to the market together. Bonnie bought 8 apples. Samuel bought 20 more apples than Bonnie. Samuel then ate half of them and used 1/7 of them to make apple pie. How many apples does Samuel have left?"""
    # Define the number of apples Bonnie bought
    bonnie_apples = 8

    # Define the number of apples Samuel bought
    samuel_apples = bonnie_apples + 20

    # Calculate the number of apples Samuel has left after eating half
    samuel_apples -= samuel_apples / 2

    # Calculate the number of apples Samuel has left after using 1/7 to make apple pie
    samuel_apples -= samuel_apples / 7

    # Display the number of apples Samuel has left
    result = samuel_apples
    return result

print(solution())