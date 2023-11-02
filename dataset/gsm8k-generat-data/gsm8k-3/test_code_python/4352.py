def solution():
    """Nathan is buying decorations for his wedding reception. The reception hall will have 20 tables. Each table needs a linen tablecloth ($25 to rent), 4 place settings ($10 each to rent), and a centerpiece. Each centerpiece will have 10 roses ($5 each) and 15 lilies ($4 each). How much will the decorations cost?"""
    # Define the cost of each rental and item
    TABLECLOTH_COST = 25
    PLACE_SETTING_COST = 10
    ROSE_COST = 5
    LILY_COST = 4

    # Define the number of tables
    NUM_TABLES = 20

    # Calculate the total cost of the tablecloths
    tablecloth_cost = NUM_TABLES * TABLECLOTH_COST

    # Calculate the total cost of the place settings
    place_setting_cost = NUM_TABLES * 4 * PLACE_SETTING_COST

    # Calculate the total cost of the roses
    rose_cost = NUM_TABLES * ROSE_COST * 10

    # Calculate the total cost of the lilies
    lily_cost = NUM_TABLES * LILY_COST * 15

    # Calculate the total cost of all the decorations
    total_cost = tablecloth_cost + place_setting_cost + rose_cost + lily_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())