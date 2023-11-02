def solution():
    # Define the weight range of the Durian
    durian_weight_range = range(2, 8)
    # Check if a Durian is heavy enough to cause injury or death if it falls on a person's head
    if max(durian_weight_range) > 10:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())