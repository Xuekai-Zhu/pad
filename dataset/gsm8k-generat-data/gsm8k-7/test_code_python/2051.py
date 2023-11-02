def solution():
    num_pies = 10
    apples_per_pie = 8
    num_existing_apples = 50

    # Calculate the total number of apples needed for all pies
    total_apples_needed = num_pies * apples_per_pie

    # Calculate the number of additional apples needed
    additional_apples_needed = total_apples_needed - num_existing_apples
    result = additional_apples_needed
    return result

print(solution())