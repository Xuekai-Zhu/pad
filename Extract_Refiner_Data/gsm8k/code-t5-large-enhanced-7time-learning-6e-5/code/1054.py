def solution():
    
    # Define the initial number of stickers
    initial_stickers = 100

    # Define the number of stickers collected last year
    last_year_stickers = 50

    # Define the number of stickers collected this year
    this_year_stickers = last_year_stickers * 2

    # Calculate the total number of stickers collected
    total_stickers = initial_stickers + last_year_stickers + this_year_stickers

    # return the result
    result = total_stickers
    return result

print(solution())