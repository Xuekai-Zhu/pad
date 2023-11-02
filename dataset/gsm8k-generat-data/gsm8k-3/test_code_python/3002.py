def solution():
    """Brenda volunteered to make 3 trays of banana pudding for the family reunion.  Each tray of banana pudding would need 80 wafer cookies.  A box of wafer cookies only had 60 cookies per box.  Each box costs $3.50.  How much will it cost her to buy just enough boxes for 3 trays of banana pudding?"""
    # Define the number of cookies needed for each tray
    COOKIES_PER_TRAY = 80

    # Calculate the total number of cookies needed
    total_cookies = COOKIES_PER_TRAY * 3

    # Calculate the number of boxes needed, rounding up to the nearest whole number
    boxes_needed = int((total_cookies + 59) / 60)

    # Calculate the total cost of the boxes of cookies
    box_cost = 3.5
    total_cost = boxes_needed * box_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())