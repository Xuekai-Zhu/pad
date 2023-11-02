def solution():
    num_boxes = 2
    num_days = 45
    box_price = 100.0
    discount = 0.1  # 10% discount

    # Calculate the total cost of one box of contacts
    total_box_cost = num_boxes * box_price * (1 - discount)

    # Calculate the total cost of two boxes of contacts
    total_cost = total_box_cost * num_days

    # Calculate the cost per pair of contacts
    cost_per_contact = total_cost / num_boxes
    result = cost_per_contact
    return result

print(solution())