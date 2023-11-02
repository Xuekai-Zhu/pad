def solution():
    # Calculate the total money Geoffrey received
    total_money = 20 + 25 + 30  

    # Calculate the money Geoffrey had before going to the video game store
    money_before_purchase = total_money  

    # Calculate the cost of 3 video games
    games_cost = 3 * 35  

    # Calculate the total amount spent by Geoffrey at the video game store
    total_spent = money_before_purchase + games_cost  

    # Calculate the money left with Geoffrey after this purchase
    money_left = 125 - total_spent  
    result = money_left
    return result

print(solution())