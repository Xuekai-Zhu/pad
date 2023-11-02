def solution():
    """Papi Calot prepared his garden to plant potatoes. He planned to plant 7 rows of 18 plants each. But he still has a bit of room left, so he’s thinking about adding 15 additional potato plants. How many plants does Papi Calot have to buy?"""
    # Define the number of rows and plants per row
    rows = 7
    plants_per_row = 18

    # Calculate the total number of plants originally planned
    total_plants = rows * plants_per_row

    # Add the additional plants
    total_plants += 15

    # Calculate the number of plants Papi Calot has to buy
    plants_to_buy = total_plants - (rows * plants_per_row)

    # return the result
    result = plants_to_buy
    return result

print(solution())