def solution():
    # Calculate the total value of one box of food and supplies
    box_value = 80 + 165

    # Calculate the total value of 400 boxes of food and supplies
    total_value = box_value * 400

    # Calculate the amount of money donated to the organization
    donated_money = total_value * 4

    # Calculate the total number of boxes the organization can pack with the donated money
    total_boxes = (donated_money + total_value) / box_value

    result = total_boxes
    return result

print(solution())