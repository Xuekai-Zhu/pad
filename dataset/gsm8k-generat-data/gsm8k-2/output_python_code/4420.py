def solution():
    """Charlotte, Lisa, and Patricia have a joint baseball collection. One of their friends is selling a rare baseball card for $100 on his website. Not wanting to miss such a rare opportunity, they have pooled all their money to buy the card. Patricia has $6. Lisa has five times Patricia’s money, but double Charlotte’s. How much more money do they require?"""
    patricia_money = 6
    lisa_money = 5 * patricia_money
    charlotte_money = 0.5 * lisa_money
    total_money = patricia_money + lisa_money + charlotte_money
    remaining_money = 100 - total_money
    result = remaining_money
    return result

print(solution())