def solution():
    """Mrs. Dunbar was creating floral arrangements for her niece's wedding.  She needed to make 5 bouquets and 7 table decorations.  She uses 12 white roses in each table decoration and 5 white roses in each bouquet.  How many white roses in total does she need to complete all bouquets and table decorations?"""
    # Define the number of white roses needed for each table decoration and bouquet
    TABLE_ROSES = 12
    BOUQUET_ROSES = 5

    # Define the number of table decorations and bouquets needed
    num_tables = 7
    num_bouquets = 5

    # Calculate the total number of white roses needed
    total_roses = (TABLE_ROSES * num_tables) + (BOUQUET_ROSES * num_bouquets)

    # Display the total number of white roses needed
    result = total_roses
    return result

print(solution())