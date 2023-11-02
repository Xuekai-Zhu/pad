def solution():
    """Roxy has 7 flowering plants in her garden. She has twice as many fruiting plants as her flowering plants. On Saturday, she goes to the nursery and buys 3 flowering plants and 2 fruiting plants. On Sunday, she gives away 1 flowering plant and 4 fruiting plants to her neighbor, Ronny. How many plants are remaining in her garden?"""
    # Define the number of flowering and fruiting plants Roxy has
    flowering_plants = 7
    fruiting_plants = 2*flowering_plants

    # Calculate the new number of flowering and fruiting plants after Saturday's purchase
    flowering_plants += 3
    fruiting_plants += 2

    # Subtract the plants given away on Sunday
    flowering_plants -= 1
    fruiting_plants -= 4

    # Calculate the total number of remaining plants
    total_plants = flowering_plants + fruiting_plants

    # Display the total number of remaining plants
    result = total_plants
    return result

print(solution())