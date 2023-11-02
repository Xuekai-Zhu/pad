def solution():
    total_amount = 10  # Adonis's dad uses a new 10 oz bottle
    hot_sauce_added = 0.5  # Adonis adds 1/2 ounce of hot sauce every day
    shampoo_used_per_day = 1  # Adonis's dad uses 1 oz of shampoo every day
    days = 4  # Adonis replaces the shampoo with hot sauce for 4 days

    # Calculate the total amount of shampoo used in 4 days
    total_shampoo_used = shampoo_used_per_day * days

    # Calculate the total amount of hot sauce added in 4 days
    total_hot_sauce_added = hot_sauce_added * days

    # Calculate the percentage of the liquid in the bottle that is hot sauce after 4 days
    percentage_hot_sauce = (total_hot_sauce_added / (total_shampoo_used + total_hot_sauce_added)) * 100
    result = percentage_hot_sauce
    return result

print(solution())