def solution():
    """Max has a collection of stamps in three colors: 20 red stamps, 80 blue stamps and 7 yellow ones. He is trying to sell the whole collection. 
    He already sold 20 red stamps for the price of $1.1 for each stamp and 80 blue stamps for the price of $0.8 for each stamp. 
    What price did he need to set for each yellow stamp to be able to earn the total of $100 from the whole sale?"""
    
    red_stamps = 20
    blue_stamps = 80
    yellow_stamps = 7
    
    red_price = 1.1
    blue_price = 0.8
    
    total_earned = (red_stamps * red_price) + (blue_stamps * blue_price)
    money_left_to_earn = 100 - total_earned
    price_per_yellow_stamp = money_left_to_earn / yellow_stamps
    
    result = price_per_yellow_stamp
    return result

print(solution())