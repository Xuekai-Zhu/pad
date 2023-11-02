def solution():
    """Roxy has 7 flowering plants in her garden.  She has twice as many fruiting plants as her flowering plants.  On Saturday, she goes to the nursery and buys 3 flowering plants and 2 fruiting plants. On Sunday, she gives away 1 flowering plant and 4 fruiting plants to her neighbor, Ronny.   How many plants are remaining in her garden?"""
    # Define the initial number of flowering plants
    flowering_plants = 7

    # Define the initial number of fruiting plants
    fruiting_plants = flowering_plants * 2

    # Add the plants bought on Saturday
    flowering_plants += 3
    fruiting_plants += 2

    # Remove the plants given away on Sunday
    flowering_plants -= 1
    fruiting_plants -= 4

    # Calculate the total number of plants remaining
    total_plants = flowering_plants + fruiting_plants

    # Return the result
    result = total_plants
    return result

print(solution())