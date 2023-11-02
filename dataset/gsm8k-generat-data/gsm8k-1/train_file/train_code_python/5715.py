def solution():
    """2 tablespoons of popcorn kernels will make 4 cups of popcorn. For movie night, Joanie wants 3 cups of popcorn, Mitchell wants 4 cups of popcorn, Miles and Davis said they would split 6 cups of popcorn and Cliff said he would only eat 3 cups. How many tablespoons of popcorn kernels will they need?"""
    tablespoons_per_cup = 0.5
    joanie_cups = 3
    mitchell_cups = 4
    miles_davis_cups = 6
    cliff_cups = 3
    total_cups = joanie_cups + mitchell_cups + miles_davis_cups + cliff_cups
    total_tablespoons = total_cups * (2 / 4)
    result = total_tablespoons
    return result

print(solution())