def solution():
    num_trucks_1 = 7
    num_boxes_1 = 20
    num_containers_per_box_1 = 8

    num_trucks_2 = 5
    num_boxes_2 = 12
    num_containers_per_box_2 = 8

    total_boxes = (num_trucks_1 * num_boxes_1) + (num_trucks_2 * num_boxes_2)
    total_containers = total_boxes * num_containers_per_box_1

    num_trucks = 10
    containers_per_truck = total_containers / num_trucks

    result = containers_per_truck
    return result

print(solution())