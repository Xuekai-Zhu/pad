def solution():
    # Define the categories of fair trade and laptops
    fair_trade_categories = ["agricultural production"]
    laptop_category = "consumer electronics"
    # Check if fair trade applies to laptops
    if laptop_category not in fair_trade_categories:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())