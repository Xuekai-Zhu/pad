def solution():
    """On a Sunday morning, Josephine sold milk in the farm stall. The buyers brought their containers. She filled three containers with two liters each, two containers with 0.75 liters each, and five containers with 0.5 liters each. How many liters of milk did Josephine sell in total?"""
    # Define the number of containers and their corresponding volumes
    containers = [3, 2, 5]
    volumes = [2, 0.75, 0.5]

    # Calculate the total volume of milk sold
    total_volume = sum([containers[i]*volumes[i] for i in range(len(containers))])

    # Return the result in liters
    result = total_volume
    return result

print(solution())