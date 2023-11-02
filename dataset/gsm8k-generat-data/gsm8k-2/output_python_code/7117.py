def solution():
    """Mrs. Dunbar was creating floral arrangements for her niece's wedding. She needed to make 5 bouquets and 7 table decorations. She uses 12 white roses in each table decoration and 5 white roses in each bouquet. How many white roses in total does she need to complete all bouquets and table decorations?"""
    white_roses_per_table = 12
    white_roses_per_bouquet = 5
    total_roses = (white_roses_per_table * 7) + (white_roses_per_bouquet * 5)
    result = total_roses
    return result

print(solution())