def solution():
    """There are 7 trucks that have 20 boxes. There are 5 trucks that have 12 boxes. Each box holds 8 containers of oil. If all of the oil is evenly redistributed onto 10 trucks, how many containers of oil will each truck have?"""
    # Calculate the total number of containers of oil
    total_containers = (7 * 20 + 5 * 12) * 8

    # Calculate the number of containers of oil per truck
    containers_per_truck = total_containers / 10

    # Display the number of containers of oil per truck
    result = containers_per_truck
    return result

print(solution())