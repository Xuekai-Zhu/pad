def solution():
    """ Aunt May milks her cows twice a day. This morning she got 365 gallons of milk. This evening she got 380 gallons. She sold 612 gallons to the local ice cream factory. She had 15 gallons left over from yesterday. How many gallons of milk does she have left?"""
    morning_milk = 365
    evening_milk = 380
    milk_sold = 612
    milk_left_yesterday = 15
    total_milk = morning_milk + evening_milk + milk_left_yesterday
    milk_left = total_milk - milk_sold
    result = milk_left
    return result

print(solution())