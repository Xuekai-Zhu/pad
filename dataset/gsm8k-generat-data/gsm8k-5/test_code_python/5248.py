def solution():
    initial_weight = 135  # John's initial squat weight was 135 pounds
    weight_increase = 265  # John increased his squat weight by 265 pounds after training
    total_weight = initial_weight + weight_increase  # John's total squat weight after training

    # Calculate the weight increase with the magical bracer
    weight_bracer = total_weight * 6  # The bracer increases his strength by 600%

    # Calculate John's total squat weight with the bracer
    total_weight_bracer = total_weight + weight_bracer
    result = total_weight_bracer
    return result

print(solution())