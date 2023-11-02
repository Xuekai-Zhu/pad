def solution():
    
    # Define the initial number of stickers
    initial_stickers = 0

    # Calculate the number of stickers given to Luis
    luis_stickers = initial_stickers / 2

    # Calculate the number of stickers given to Kris
    kris_stickers = 9

    # Calculate the number of stickers given to Rob
    rob_stickers = 7

    # Calculate the number of stickers given to Seth
    seth_stickers = luis_stickers / 2

    # Calculate the number of stickers Seth had in the beginning
    seth_stickers = seth_stickers + kris_stickers - rob_stickers

    # Display the number of stickers Seth had in the beginning
    result = seth_stickers
    return result

print(solution())