def solution():
    """Eric sorted 150 colored pencils into 5 containers for his art class. Before class, another teacher brought him 30 more pencils. How many can he evenly distribute between the five containers now?"""
    total_pencils = 150 + 30
    containers = 5
    pencils_per_container = total_pencils // containers
    remaining_pencils = total_pencils % containers
    result = pencils_per_container
    return result

print(solution())