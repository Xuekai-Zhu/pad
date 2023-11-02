def solution():
    cheesecakes_on_display = 10
    cheesecakes_in_fridge = 15
    cheesecakes_sold = 7

    # Calculate the total number of cheesecakes available
    total_cheesecakes = cheesecakes_on_display + cheesecakes_in_fridge

    # Calculate the number of cheesecakes left to be sold
    cheesecakes_left = total_cheesecakes - cheesecakes_sold
    result = cheesecakes_left
    return result

print(solution())