def solution():
    # Calculate the amount of shampoo used in 4 days
    shampoo_used = 4 * 1  # the dad uses 1 oz of shampoo a day
    hot_sauce_added = 4 * (1/2)  # Adonis replaces the shampoo with 1/2 oz of hot sauce every day
    total_liquid = 10 - shampoo_used  # the total amount of liquid left in the bottle after 4 days
    hot_sauce_percentage = (hot_sauce_added / total_liquid) * 100

    result = hot_sauce_percentage
    return result

print(solution())