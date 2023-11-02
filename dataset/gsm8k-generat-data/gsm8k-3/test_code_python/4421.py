def solution():
    """Charlotte, Lisa, and Patricia have a joint baseball collection. One of their friends is selling a rare baseball card for $100 on his website. Not wanting to miss such a rare opportunity, they have pooled all their money to buy the card. Patricia has $6. Lisa has five times Patricia’s money, but double Charlotte’s. How much more money do they require?"""
    # Define the cost of the rare baseball card
    card_cost = 100

    # Define the money each person has
    patricia_money = 6
    lisa_money = 5 * patricia_money
    charlotte_money = lisa_money / 2

    # Calculate the total money they have
    total_money = patricia_money + lisa_money + charlotte_money

    # Calculate the remaining money they need to buy the card
    remaining_money = card_cost - total_money

    # Display the remaining money needed
    result = remaining_money
    return result

print(solution())