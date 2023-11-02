def solution():
    """Nathan is buying decorations for his wedding reception. The reception hall will have 20 tables. Each table needs a linen tablecloth ($25 to rent), 4 place settings ($10 each to rent), and a centerpiece. Each centerpiece will have 10 roses ($5 each) and 15 lilies ($4 each). How much will the decorations cost?"""
    num_tables = 20
    linen_cost = 25
    place_setting_cost = 10
    num_roses = 10
    rose_cost = 5
    num_lilies = 15
    lily_cost = 4
    
    total_cost = (linen_cost + (4 * place_setting_cost) + ((num_roses * rose_cost) + (num_lilies * lily_cost))) * num_tables
    result = total_cost
    return result

print(solution())