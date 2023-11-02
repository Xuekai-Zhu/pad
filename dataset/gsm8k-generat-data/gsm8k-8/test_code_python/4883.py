def solution():
    # Calculate the cost of the doctor's exam
    exam_cost = 300 / 60 * 0.5 + 150

    # Calculate the total cost of the visit
    total_cost = 1200 + exam_cost

    # Calculate the amount insurance covers
    insurance_covered = total_cost * 0.8

    # Calculate the amount Tim pays out of pocket
    out_of_pocket = total_cost - insurance_covered
    result = out_of_pocket
    return result

print(solution())