def solution():
    """Tommy ordered a total weight of 10 kilograms of apple, orange, grape, and strawberry fruits. He ordered 3 kilograms of apples, 1 kilogram of orange, and 3 kilograms of grapes. How many kilograms of strawberries did he order?"""
    # Define the total weight and weight of each type of fruit ordered
    total_weight = 10
    apple_weight = 3
    orange_weight = 1
    grape_weight = 3

    # Calculate the weight of strawberries ordered
    strawberry_weight = total_weight - apple_weight - orange_weight - grape_weight

    # Display the weight of strawberries ordered
    result = strawberry_weight
    return result

print(solution())