def solution():
    """Mrs. Dunbar was creating floral arrangements for her niece's wedding. She needed to make 5 bouquets and 7 table decorations. She uses 12 white roses in each table decoration and 5 white roses in each bouquet. How many white roses in total does she need to complete all bouquets and table decorations?"""
    # Define the number of bouquets and table decorations
    num_bouquets = 5
    num_tables = 7

    # Define the number of white roses in each bouquet and table decoration
    roses_per_bouquet = 5
    roses_per_table = 12

    # Calculate the total number of white roses needed
    total_roses = (num_bouquets * roses_per_bouquet) + (num_tables * roses_per_table)

    # return the result
    result = total_roses
    return result

print(solution())