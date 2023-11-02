def solution():
    """There are 7 trucks that have 20 boxes. There are 5 trucks that have 12 boxes. Each box holds 8 containers of oil. If all of the oil is evenly redistributed onto 10 trucks, how many containers of oil will each truck have?"""
    boxes_on_7_trucks = 7 * 20
    boxes_on_5_trucks = 5 * 12
    total_boxes = boxes_on_7_trucks + boxes_on_5_trucks
    containers_per_box = 8
    total_containers = total_boxes * containers_per_box
    trucks = 10
    containers_per_truck = total_containers / trucks
    result = containers_per_truck
    return result

print(solution())