def solution():
    display_cheesecakes = 10  # There are 10 cheesecakes on the display
    fridge_cheesecakes = 15  # There are 15 cheesecakes in the fridge
    sold_cheesecakes = 7  # 7 cheesecakes have already been sold from the display

    # Calculate the total number of cheesecakes available
    total_cheesecakes = display_cheesecakes + fridge_cheesecakes

    # Calculate the number of cheesecakes left to be sold
    remaining_cheesecakes = total_cheesecakes - sold_cheesecakes
    result = remaining_cheesecakes
    return result

print(solution())