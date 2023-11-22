def solution():
    
    # Define the initial number of stickers
    initial_stickers = 10

    # Define the number of stickers Charlie bought from the store
    bought_stickers = 21

    # Define the number of stickers Charlie got for his birthday
    birthday_stickers = 23

    # Calculate the total number of stickers Charlie has
    total_stickers = initial_stickers + bought_stickers + birthday_stickers

    # Subtract the stickers Charlie gave to his sister
    total_stickers -= 9

    # Subtract the stickers Charlie used to decorate a greeting card
    total_stickers -= 28

    # Display the total number of stickers Charlie has left
    result = total_stickers
    return result

print(solution())