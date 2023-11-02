def solution():
    treshawn = 1/2
    michael = 1/3
    lamar = 1/6

    # Calculate the total amount of pizza needed
    total_pizza = treshawn + michael + lamar

    # Round up to the nearest whole pizza
    num_pizzas = math.ceil(total_pizza)

    result = num_pizzas
    return result

print(solution())