def solution():
    """A group of friends walked into Juju’s Juice Bar ordered a glass of fruit juice each. They spent a total of $94. Some of them ordered mango juice, which sells for $5 a glass, while others asked for pineapple juice, at $6 a glass. If $54 was spent on pineapple juice, how many people were in the group?"""
    pineapple_price = 6
    mango_price = 5
    total_price = 94
    pineapple_spending = 54
    mango_spending = total_price - pineapple_spending
    pineapple_count = pineapple_spending / pineapple_price
    mango_count = mango_spending / mango_price
    total_people = pineapple_count + mango_count
    result = total_people
    return result

print(solution())