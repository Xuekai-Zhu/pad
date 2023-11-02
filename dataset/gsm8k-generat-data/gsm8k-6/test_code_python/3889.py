def solution():
    # Calculate the total number of pencils that Louise has
    total_pencils = 20 + 2*20 + 40 + (20+2*20)  # red: 20, blue: 2*20, yellow: 40, green: red+blue

    # Calculate the total number of boxes needed
    total_boxes = total_pencils // 20  # each box holds 20 pencils

    result = total_boxes
    return result

print(solution())