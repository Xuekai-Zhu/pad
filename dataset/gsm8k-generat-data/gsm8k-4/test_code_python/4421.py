def solution():
    """Charlotte, Lisa, and Patricia have a joint baseball collection. One of their friends is selling a rare baseball card for $100 on his website. Not wanting to miss such a rare opportunity, they have pooled all their money to buy the card. Patricia has $6. Lisa has five times Patricia’s money, but double Charlotte’s. How much more money do they require?"""
    # Define the price of the baseball card
    card_price = 100

    # Calculate the amount of money each person has
    patricia_money = 6
    lisa_money = 5 * patricia_money
    charlotte_money = lisa_money / 2

    # Calculate the total amount of money they have
    total_money = patricia_money + lisa_money + charlotte_money

    # Calculate the amount of money they need to buy the card
    needed_money = card_price - total_money

    result = needed_money
    return result

print(solution())