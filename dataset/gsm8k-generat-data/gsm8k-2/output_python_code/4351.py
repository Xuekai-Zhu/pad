def solution():
    """Nathan is buying decorations for his wedding reception. The reception hall will have 20 tables. Each table needs a linen tablecloth ($25 to rent), 4 place settings ($10 each to rent), and a centerpiece. Each centerpiece will have 10 roses ($5 each) and 15 lilies ($4 each). How much will the decorations cost?"""
    num_tables = 20
    tablecloth_rental = 25
    place_setting_rental = 10
    num_roses_per_centerpiece = 10
    rose_price = 5
    num_lilies_per_centerpiece = 15
    lily_price = 4

    total_cost_per_table = (
            tablecloth_rental
            + (4 * place_setting_rental)
            + (num_roses_per_centerpiece * rose_price)
            + (num_lilies_per_centerpiece * lily_price)
    )
    total_cost = num_tables * total_cost_per_table
    result = total_cost
    return result

print(solution())