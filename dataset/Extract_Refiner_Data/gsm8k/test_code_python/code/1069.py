def solution():
    
    # Define the total number of bananas and the number of bananas eaten by the first monkey
    total_bananas = 315
    first_monkey_bananas = 10

    # Calculate the number of bananas eaten by the second monkey
    second_monkey_bananas = first_monkey_bananas + 4

    # Calculate the number of bananas eaten by the third monkey
    third_monkey_bananas = total_bananas - first_monkey_bananas - second_monkey_bananas

    # Calculate the number of bananas eaten by the third monkey
    third_monkey_bananas = third_monkey_bananas / 1

    # Return the result
    result = third_monkey_bananas
    return result

print(solution())