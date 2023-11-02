def solution():
    """Donna worked 2 hours every morning walking dogs in her neighborhood for $10.00 an hour.  5 days a week, after school, she worked at a card shop for 2 hours and made $12.50 an hour.  On the weekends, she usually made $10.00 an hour babysitting and was guaranteed 4 hours every Saturday from her neighbor.  How much money did she make over 7 days?"""
    # Calculate Donna's earnings from dog walking
    dog_walking_hours = 2 * 5 * 7 # 2 hours per day for 5 days a week for 7 days
    dog_walking_pay = 10 * dog_walking_hours

    # Calculate Donna's earnings from working at the card shop
    card_shop_hours = 2 * 5 # 2 hours per day for 5 days a week
    card_shop_pay = 12.5 * card_shop_hours

    # Calculate Donna's earnings from babysitting
    babysitting_hours = 4 + 10 * 2 # 4 hours on Saturday plus 10 hours on Sunday
    babysitting_pay = 10 * babysitting_hours

    # Calculate Donna's total earnings
    total_earnings = dog_walking_pay + card_shop_pay + babysitting_pay

    # Display Donna's total earnings
    result = total_earnings
    return result

print(solution())