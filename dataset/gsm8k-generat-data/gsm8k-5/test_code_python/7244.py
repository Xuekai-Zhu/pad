def solution():
    green_buttons = 90  # The tailor bought 90 green buttons
    yellow_buttons = green_buttons + 10  # She bought 10 more yellow buttons than green buttons
    blue_buttons = green_buttons - 5  # She bought 5 fewer blue buttons than green buttons

    # Calculate the total number of buttons purchased
    total_buttons = green_buttons + yellow_buttons + blue_buttons
    result = total_buttons
    return result

print(solution())