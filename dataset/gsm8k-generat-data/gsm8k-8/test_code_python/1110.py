def solution():
    # Define the weight of the child and the total amount of medicine needed
    weight = 30
    total_medicine = weight * 5 * 3

    # Calculate the amount of medicine needed for each of the three parts
    medicine_per_part = total_medicine / 3

    result = medicine_per_part
    return result

print(solution())