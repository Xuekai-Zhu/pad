def solution():
    """A tailor purchased buttons for the clothes. She bought 90 green buttons, 10 more yellow buttons than the green buttons, and 5 fewer blue buttons than the green buttons. How many buttons did the tailor purchase?"""
    # Define the number of green buttons purchased
    green_buttons = 90
    
    # Calculate the number of yellow buttons purchased
    yellow_buttons = green_buttons + 10
    
    # Calculate the number of blue buttons purchased
    blue_buttons = green_buttons - 5
    
    # Calculate the total number of buttons purchased
    total_buttons = green_buttons + yellow_buttons + blue_buttons
    
    # return the result
    result = total_buttons
    return result

print(solution())