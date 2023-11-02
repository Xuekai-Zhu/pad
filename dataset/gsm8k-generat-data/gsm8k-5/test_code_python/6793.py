def solution():
    # Calculate the total number of boxes and containers of oil
    total_boxes = 7 * 20 + 5 * 12  # 7 trucks with 20 boxes each, and 5 trucks with 12 boxes each
    total_containers = total_boxes * 8  # Each box holds 8 containers of oil

    # Calculate the number of containers of oil per truck after redistribution
    containers_per_truck = total_containers / 10

    result = containers_per_truck
    return result

print(solution())