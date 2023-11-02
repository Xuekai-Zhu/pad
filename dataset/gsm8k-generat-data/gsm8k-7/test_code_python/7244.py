def solution():
    num_green_buttons = 90
    num_yellow_buttons = num_green_buttons + 10
    num_blue_buttons = num_green_buttons - 5

    # Calculate the total number of buttons purchased
    total_buttons_purchased = num_green_buttons + num_yellow_buttons + num_blue_buttons
    result = total_buttons_purchased
    return result

print(solution())