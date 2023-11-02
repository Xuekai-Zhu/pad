def solution():
    """Donna worked 2 hours every morning walking dogs in her neighborhood for $10.00 an hour. 5 days a week, after school, she worked at a card shop for 2 hours and made $12.50 an hour. On the weekends, she usually made $10.00 an hour babysitting and was guaranteed 4 hours every Saturday from her neighbor. How much money did she make over 7 days?"""
    
    dog_walking_pay = 10 * 2 * 5
    card_shop_pay = 12.5 * 2 * 5
    babysitting_pay = (10 * 4) + (10 * 3)
    total_pay = dog_walking_pay + card_shop_pay + babysitting_pay
    
    result = total_pay
    return result

print(solution())