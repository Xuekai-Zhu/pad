def solution():
    # Calculate the total cost of Tim's doctor's visit after insurance coverage
    doctor_cost = 300 * (1 - 0.75)  # 75% of the cost is covered by insurance

    # Calculate the total cost of the cat's visit after pet insurance coverage
    cat_cost = 120 - 60  # $60 is covered by pet insurance

    # Calculate the total amount Tim paid
    total_cost = doctor_cost + cat_cost
    result = total_cost
    return result

print(solution())