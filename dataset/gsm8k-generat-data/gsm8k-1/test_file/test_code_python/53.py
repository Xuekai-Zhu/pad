def solution():
    """A wooden bridge can carry no more than 5000 pounds. A delivery truck filled with identical boxes, each weighing 15 pounds, will pass over the bridge. The combined weight of the driver and the empty truck is 3755 pounds. What is the maximum number of boxes which can be loaded onto the truck while not exceeding the bridge's weight limit?"""
    bridge_weight_limit = 5000
    driver_and_truck_weight = 3755
    box_weight = 15
    max_boxes = (bridge_weight_limit - driver_and_truck_weight) // box_weight
    result = max_boxes
    return result

print(solution())