def solution():
    """Max has a collection of stamps in three colors: 20 red stamps, 80 blue stamps and 7 yellow ones. He is trying to sell the whole collection. He already sold 20 red stamps for the price of $1.1 for each stamp and 80 blue stamps for the price of $0.8 for each stamp. What price did he need to set for each yellow stamp to be able to earn the total of $100 from the whole sale?"""
    # Define the number of stamps and their prices
    red_stamps = 20
    blue_stamps = 80
    yellow_stamps = 7
    red_price = 1.1
    blue_price = 0.8

    # Calculate the total earned from the red and blue stamps
    red_earned = red_stamps * red_price
    blue_earned = blue_stamps * blue_price
    total_earned = red_earned + blue_earned

    # Calculate the total amount needed from selling the yellow stamps
    yellow_needed = 100 - total_earned
    yellow_price = yellow_needed / yellow_stamps

    # Display the price needed for each yellow stamp
    result = yellow_price
    return result

print(solution())