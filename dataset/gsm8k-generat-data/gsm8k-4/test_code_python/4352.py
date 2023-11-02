def solution():
    """Nathan is buying decorations for his wedding reception. The reception hall will have 20 tables. Each table needs a linen tablecloth ($25 to rent), 4 place settings ($10 each to rent), and a centerpiece. Each centerpiece will have 10 roses ($5 each) and 15 lilies ($4 each). How much will the decorations cost?"""
    # Define the cost of renting a tablecloth, a place setting, a rose, and a lily
    TABLECLOTH_RENTAL_COST = 25
    PLACE_SETTING_RENTAL_COST = 10
    ROSE_COST = 5
    LILY_COST = 4

    # Define the number of tables and items needed per table
    NUM_TABLES = 20
    NUM_PLACE_SETTINGS_PER_TABLE = 4
    NUM_ROSES_PER_CENTERPIECE = 10
    NUM_LILIES_PER_CENTERPIECE = 15

    # Calculate the total cost of renting tablecloths and place settings
    rental_cost_per_table = TABLECLOTH_RENTAL_COST + (NUM_PLACE_SETTINGS_PER_TABLE * PLACE_SETTING_RENTAL_COST)
    total_rental_cost = rental_cost_per_table * NUM_TABLES

    # Calculate the total cost of all the centerpieces
    total_roses_cost = NUM_ROSES_PER_CENTERPIECE * (NUM_TABLES * 2) * ROSE_COST  # 2 centerpieces per table
    total_lilies_cost = NUM_LILIES_PER_CENTERPIECE * (NUM_TABLES * 2) * LILY_COST  # 2 centerpieces per table
    total_centerpieces_cost = total_roses_cost + total_lilies_cost

    # Calculate the total cost of decorations
    total_cost = total_rental_cost + total_centerpieces_cost

    result = total_cost
    return result

print(solution())