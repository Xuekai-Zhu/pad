def solution():
    """Brenda volunteered to make 3 trays of banana pudding for the family reunion. Each tray of banana pudding would need 80 wafer cookies. A box of wafer cookies only had 60 cookies per box. Each box costs $3.50. How much will it cost her to buy just enough boxes for 3 trays of banana pudding?"""
    # Define the number of cookies needed for each tray
    cookies_per_tray = 80

    # Calculate the total number of cookies needed for 3 trays
    total_cookies = cookies_per_tray * 3

    # Calculate the number of boxes needed to buy
    boxes_needed = int(total_cookies / 60) + 1

    # Calculate the total cost of buying the boxes
    total_cost = boxes_needed * 3.50

    # Display the total cost
    result = total_cost
    return result

print(solution())