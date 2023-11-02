def solution():
    max_weight = 5000  # The wooden bridge can carry no more than 5000 pounds
    weight_per_box = 15  # Each box weighs 15 pounds
    combined_weight = 3755  # The combined weight of the truck and the empty truck is 3755 pounds

    # Calculate the maximum number of boxes that can be loaded onto the truck
    max_boxes = (combined_weight - weight_per_box) / weight_per_box
    result = max_boxes
    return result

print(solution())