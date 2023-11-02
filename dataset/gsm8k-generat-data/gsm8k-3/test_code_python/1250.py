def solution():
    """Lucia is a dancer. She takes 2 hip-hop classes a week, 2 ballet classes a week, and 1 jazz class a week. One hip-hop class costs $10. One ballet class costs $12, and one jazz class costs $8. What is the total cost of Lucia’s dance classes in one week?"""
    # Define the cost of each type of dance class
    HIPHOP_COST = 10
    BALLET_COST = 12
    JAZZ_COST = 8

    # Define the number of each type of dance class taken per week
    hiphop_classes = 2
    ballet_classes = 2
    jazz_classes = 1

    # Calculate the total cost of the hip-hop classes
    hiphop_cost = hiphop_classes * HIPHOP_COST

    # Calculate the total cost of the ballet classes
    ballet_cost = ballet_classes * BALLET_COST

    # Calculate the total cost of the jazz classes
    jazz_cost = jazz_classes * JAZZ_COST

    # Calculate the total cost of all the dance classes
    total_cost = hiphop_cost + ballet_cost + jazz_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())