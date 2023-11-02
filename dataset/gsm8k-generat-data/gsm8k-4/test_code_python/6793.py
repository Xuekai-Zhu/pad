def solution():
    """There are 7 trucks that have 20 boxes. There are 5 trucks that have 12 boxes. Each box holds 8 containers of oil. If all of the oil is evenly redistributed onto 10 trucks, how many containers of oil will each truck have?"""
    # Define the total number of trucks and boxes
    total_trucks = 12
    total_boxes = 7 * 20 + 5 * 12

    # Define the number of containers per box
    containers_per_box = 8

    # Calculate the total number of containers
    total_containers = total_boxes * containers_per_box

    # Calculate the number of containers per truck
    containers_per_truck = total_containers / total_trucks

    # Return the result
    result = containers_per_truck
    return result

print(solution())