def solution():
    """Adonis is playing a prank on his dad by replacing his shampoo with hot sauce. Every day, after his dad showers, Adonis replaces the shampoo with 1/2 an ounce of hot sauce. He knows his dad uses 1 oz of shampoo a day from a new 10 oz bottle that no one else uses. After 4 days, what percentage of the liquid in the bottle is hot sauce?"""
    total_shampoo = 10
    daily_shampoo = 1
    hot_sauce = 0.5
    for i in range(4):
        total_shampoo -= daily_shampoo
        total_shampoo += hot_sauce
    hot_sauce_percentage = (hot_sauce * 4 / total_shampoo) * 100

    result = hot_sauce_percentage
    return result

print(solution())