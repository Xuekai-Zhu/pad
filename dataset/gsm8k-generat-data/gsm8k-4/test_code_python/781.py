def solution():
    """I went to the music shop and there were CDs of The Life Journey for $100, A Day a Life for $50, and When You Rescind for $85 on display. If I bought 3 of each CD to share with my friends, what's the total amount of money I spent in the shop?"""
    # Define the prices of each CD and the quantity purchased
    life_journey_price = 100
    day_a_life_price = 50
    when_you_rescind_price = 85
    quantity = 3

    # Calculate the total amount spent
    total_amount = (life_journey_price + day_a_life_price + when_you_rescind_price) * quantity

    # return the result
    result = total_amount
    return result

print(solution())