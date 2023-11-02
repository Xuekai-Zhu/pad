def solution():
    # Initialize the number of topping combinations to zero
    num_combinations = 0

    # Iterate through each cheese option
    for cheese in range(3):
        # Iterate through each meat option
        for meat in range(4):
            # Iterate through each vegetable option
            for veg in range(5):
                # Check if the combination includes both peppers and pepperoni
                if veg == 3 and meat == 1:
                    continue  # Skip this combination
                else:
                    num_combinations += 1  # Add this combination to the total

    result = num_combinations
    return result

print(solution())