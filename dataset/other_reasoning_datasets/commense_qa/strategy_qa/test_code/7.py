def solution():
    # Define the admission rates of Princeton and UPenn
    princeton_admission_rate = 0.06
    upenn_admission_rate = 0.09
    # Check if Brooke Shields could succeed at UPenn
    if upenn_admission_rate <= princeton_admission_rate:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())