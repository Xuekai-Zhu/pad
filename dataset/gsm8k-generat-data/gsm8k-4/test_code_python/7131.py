def solution():
    """Donna worked 2 hours every morning walking dogs in her neighborhood for $10.00 an hour.  5 days a week, after school, she worked at a card shop for 2 hours and made $12.50 an hour.  On the weekends, she usually made $10.00 an hour babysitting and was guaranteed 4 hours every Saturday from her neighbor.  How much money did she make over 7 days?"""
    # Define the hourly rates and hours worked for each job
    dog_walking_rate = 10
    dog_walking_hours = 2

    card_shop_rate = 12.5
    card_shop_hours = 2
    card_shop_days = 5

    babysitting_rate = 10
    babysitting_hours = 4
    babysitting_days = 2

    # Calculate the total earnings for each job
    dog_walking_earnings = dog_walking_rate * dog_walking_hours * 7

    card_shop_earnings = card_shop_rate * card_shop_hours * card_shop_days

    babysitting_earnings = (babysitting_rate * babysitting_hours) + (babysitting_rate * babysitting_hours * babysitting_days)

    # Calculate the total earnings over 7 days
    total_earnings = dog_walking_earnings + card_shop_earnings + babysitting_earnings

    # Return the result
    result = total_earnings
    return result

print(solution())