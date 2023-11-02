def solution():
    """A fruit basket consists of 4 bananas, 3 apples, 24 strawberries, 2 avocados, and a bunch of grapes. One banana costs $1. An apple costs $2. 12 strawberries cost $4. An avocado costs $3, and half a bunch of grapes costs $2. What is the total cost of the fruit basket?"""
    # Calculate the cost of bananas
    banana_cost = 4 * 1

    # Calculate the cost of apples
    apple_cost = 3 * 2

    # Calculate the cost of strawberries
    strawberry_cost = (24 // 12) * 4

    # Calculate the cost of avocados
    avocado_cost = 2 * 3

    # Calculate the cost of grapes
    grapes_cost = 2 * 2

    # Calculate the total cost of the fruit basket
    total_cost = banana_cost + apple_cost + strawberry_cost + avocado_cost + grapes_cost

    result = total_cost
    return result

print(solution())