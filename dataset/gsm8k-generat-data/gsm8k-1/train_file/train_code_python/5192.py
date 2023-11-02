def solution():
    """Roxy has 7 flowering plants in her garden. She has twice as many fruiting plants as her flowering plants. On Saturday, she goes to the nursery and buys 3 flowering plants and 2 fruiting plants. On Sunday, she gives away 1 flowering plant and 4 fruiting plants to her neighbor, Ronny. How many plants are remaining in her garden?"""
    flowering_plants = 7
    fruiting_plants = 2 * flowering_plants
    new_flowering_plants = 3
    new_fruiting_plants = 2
    given_flowering_plants = 1
    given_fruiting_plants = 4
    remaining_flowering_plants = flowering_plants + new_flowering_plants - given_flowering_plants
    remaining_fruiting_plants = fruiting_plants + new_fruiting_plants - given_fruiting_plants
    result = remaining_flowering_plants + remaining_fruiting_plants
    return result

print(solution())