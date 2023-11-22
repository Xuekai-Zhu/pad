def solution():
    
    # Define the initial number of stickers
    initial_stickers = 0

    # Calculate the number of stickers Seth gave to Luis
    luis_stickers = initial_stickers / 2

    # Calculate the number of stickers Seth gave to Kris
    kris_stickers = initial_stickers - luis_stickers

    # Calculate the number of stickers Kris kept
    kris_kept_stickers = 9

    # Calculate the number of stickers Rob gave to Rob
    rob_stickers = 7

    # Calculate the total number of stickers Seth had in the beginning
    total_stickers = luis_stickers + kris_stickers + rob_stickers

    # Display the total number of stickers
    result = total_stickers
    return result

print(solution())