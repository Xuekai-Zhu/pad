def solution():
    num_bananas = 4
    banana_price = 1

    num_apples = 3
    apple_price = 2

    num_strawberries = 24
    strawberry_price = 4 / 12  # 12 strawberries cost $4

    num_avocados = 2
    avocado_price = 3

    grapes_price = 2 / 2  # half a bunch of grapes costs $2

    # Calculate the total cost of all bananas
    total_banana_cost = num_bananas * banana_price

    # Calculate the total cost of all apples
    total_apple_cost = num_apples * apple_price

    # Calculate the total cost of all strawberries
    total_strawberry_cost = num_strawberries * strawberry_price

    # Calculate the total cost of all avocados
    total_avocado_cost = num_avocados * avocado_price

    # Calculate the total cost of grapes
    total_grapes_cost = grapes_price

    # Calculate the total cost of the fruit basket
    total_cost = total_banana_cost + total_apple_cost + total_strawberry_cost + total_avocado_cost + total_grapes_cost
    result = total_cost
    return result

print(solution())