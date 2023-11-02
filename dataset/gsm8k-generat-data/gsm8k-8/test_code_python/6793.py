def solution():
    # Calculate the total number of boxes of oil
    total_boxes = (7 * 20) + (5 * 12)

    # Calculate the total number of containers of oil
    total_containers = total_boxes * 8

    # Calculate the number of containers of oil per truck
    containers_per_truck = total_containers / 10
    result = containers_per_truck
    return result

print(solution())