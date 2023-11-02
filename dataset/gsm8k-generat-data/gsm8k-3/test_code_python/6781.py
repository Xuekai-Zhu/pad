def solution():
    """Papi Calot prepared his garden to plant potatoes. He planned to plant 7 rows of 18 plants each. But he still has a bit of room left, so he’s thinking about adding 15 additional potato plants. How many plants does Papi Calot have to buy?"""
    # Define the number of rows and plants per row that Papi Calot planned to plant
    rows_planned = 7
    plants_per_row_planned = 18

    # Calculate the total number of plants that Papi Calot planned to plant
    plants_planned = rows_planned * plants_per_row_planned

    # Calculate the total number of plants that Papi Calot will have after adding the additional plants
    plants_total = plants_planned + 15

    # Calculate the number of plants Papi Calot needs to buy
    plants_to_buy = plants_total - plants_planned

    # Display the number of plants to buy
    result = plants_to_buy
    return result

print(solution())