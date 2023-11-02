def solution():
    num_peach_pies = 5
    num_apple_pies = 4
    num_blueberry_pies = 3
    fruit_per_pie = 3

    peach_price = 2.0
    apple_price = 1.0
    blueberry_price = 1.0

    # Calculate the total weight of fruit needed for all pies
    total_fruit_weight = (num_peach_pies + num_apple_pies + num_blueberry_pies) * fruit_per_pie

    # Calculate the total cost of all peaches needed
    peach_cost = num_peach_pies * fruit_per_pie * peach_price

    # Calculate the total cost of all apples needed
    apple_cost = num_apple_pies * fruit_per_pie * apple_price

    # Calculate the total cost of all blueberries needed
    blueberry_cost = num_blueberry_pies * fruit_per_pie * blueberry_price

    # Calculate the total cost of all fruit
    total_cost = peach_cost + apple_cost + blueberry_cost
    result = total_cost
    return result

print(solution())