def solution():
    """A tailor purchased buttons for the clothes. She bought 90 green buttons, 10 more yellow buttons than the green buttons, and 5 fewer blue buttons than the green buttons. How many buttons did the tailor purchase?"""
    green_buttons = 90
    yellow_buttons = green_buttons + 10
    blue_buttons = green_buttons - 5
    total_buttons = green_buttons + yellow_buttons + blue_buttons
    result = total_buttons
    return result

print(solution())