def solution():
    
    # Define the initial number of stickers
    small_stickers = 30
    large_stickers = 40

    # Calculate the number of stickers that Lorraine trades for large buttons
    large_buttons_small = large_stickers * 0.9
    large_buttons_large = large_stickers * 0.5

    # Calculate the number of stickers that Lorraine trades for small buttons
    small_buttons_large = small_stickers - large_buttons_small

    # Calculate the total number of stickers that Lorraine has
    total_stickers = small_stickers + large_stickers

    # Calculate the number of buttons Lorraine has after the trades for large buttons
    total_buttons = (small_buttons_large + large_buttons_large) * 2

    # Display the total number of buttons
    result = total_buttons
    return result

print(solution())