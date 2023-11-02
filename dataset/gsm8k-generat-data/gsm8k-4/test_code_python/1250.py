def solution():
    """Lucia is a dancer. She takes 2 hip-hop classes a week, 2 ballet classes a week, and 1 jazz class a week. One hip-hop class costs $10. One ballet class costs $12, and one jazz class costs $8. What is the total cost of Lucia’s dance classes in one week?"""
    # Define the cost of each type of class
    hip_hop_cost = 10
    ballet_cost = 12
    jazz_cost = 8

    # Define the number of classes of each type
    hip_hop_classes = 2
    ballet_classes = 2
    jazz_classes = 1

    # Calculate the total cost of Lucia's dance classes
    total_cost = (hip_hop_cost * hip_hop_classes) + (ballet_cost * ballet_classes) + (jazz_cost * jazz_classes)

    result = total_cost
    return result

print(solution())