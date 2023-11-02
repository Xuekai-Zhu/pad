def solution():
    """Tom's fruit bowl contains 3 oranges and 6 lemons. After Tom eats 3 of the fruits, how many fruits remain in Tom's fruit bowl?"""
    num_oranges = 3
    num_lemons = 6
    num_fruits_eaten = 3
    total_fruits = num_oranges + num_lemons
    remaining_fruits = total_fruits - num_fruits_eaten
    result = remaining_fruits
    return result

print(solution())