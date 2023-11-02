def solution():
    """Mrs. Dunbar was creating floral arrangements for her niece's wedding. She needed to make 5 bouquets and 7 table decorations. She uses 12 white roses in each table decoration and 5 white roses in each bouquet. How many white roses in total does she need to complete all bouquets and table decorations?"""
    bouquets = 5
    table_decorations = 7
    roses_per_table_decoration = 12
    roses_per_bouquet = 5
    total_roses = (table_decorations * roses_per_table_decoration) + (bouquets * roses_per_bouquet)
    result = total_roses
    return result

print(solution())