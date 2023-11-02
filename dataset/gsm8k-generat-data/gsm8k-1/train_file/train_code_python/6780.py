def solution():
    """Papi Calot prepared his garden to plant potatoes. He planned to plant 7 rows of 18 plants each. But he still has a bit of room left, so he’s thinking about adding 15 additional potato plants. How many plants does Papi Calot have to buy?"""
    planned_rows = 7
    planned_plants_per_row = 18
    additional_plants = 15
    total_plants = planned_rows * planned_plants_per_row + additional_plants
    plants_to_buy = total_plants - planned_rows * planned_plants_per_row
    result = plants_to_buy
    return result

print(solution())