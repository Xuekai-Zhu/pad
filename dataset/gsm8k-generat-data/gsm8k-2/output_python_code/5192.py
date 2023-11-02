def solution():
    """Roxy has 7 flowering plants in her garden. She has twice as many fruiting plants as her flowering plants. On Saturday, she goes to the nursery and buys 3 flowering plants and 2 fruiting plants. On Sunday, she gives away 1 flowering plant and 4 fruiting plants to her neighbor, Ronny. How many plants are remaining in her garden?"""
    flowering_plants = 7
    fruiting_plants = 2 * flowering_plants
    saturday_plants = 3 + 2
    sunday_plants = 1 + 4
    total_plants = flowering_plants + fruiting_plants + saturday_plants - sunday_plants
    result = total_plants
    return result

print(solution())