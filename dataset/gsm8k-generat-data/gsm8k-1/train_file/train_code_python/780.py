def solution():
    """I went to the music shop and there were CDs of The Life Journey for $100, 
    A Day a Life for $50, and When You Rescind for $85 on display.
    If I bought 3 of each CD to share with my friends, what's the total amount of money I spent in the shop?"""
    the_life_journey_price = 100
    a_day_a_life_price = 50
    when_you_rescind_price = 85
    cds_per_album = 3
    total_spent = (the_life_journey_price + a_day_a_life_price + when_you_rescind_price) * cds_per_album
    result = total_spent
    return result

print(solution())