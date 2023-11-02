def solution():
    """A fruit basket consists of 4 bananas, 3 apples, 24 strawberries, 2 avocados, and a bunch of grapes. One banana costs $1. An apple costs $2. 12 strawberries cost $4. An avocado costs $3, and half a bunch of grapes costs $2. What is the total cost of the fruit basket?"""
    banana_cost = 4 * 1
    apple_cost = 3 * 2
    strawberry_cost = (24 // 12) * 4
    avocado_cost = 2 * 3
    grapes_cost = 2 * 2
    total_cost = banana_cost + apple_cost + strawberry_cost + avocado_cost + grapes_cost
    result = total_cost
    return result

print(solution())