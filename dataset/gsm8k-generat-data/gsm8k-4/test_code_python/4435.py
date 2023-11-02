def solution():
    """Steve bought $25 worth of groceries. He bought a gallon of milk for $3, two boxes of cereal for $3.5 each, 4 bananas for $.25 each, four apples that cost $.5 each and a number of boxes of cookies. The cookies cost twice as much per box as the gallon of milk. How many boxes of cookies did he get?"""
    # Define the cost of each item
    milk_cost = 3
    cereal_cost = 3.5
    banana_cost = 0.25
    apple_cost = 0.5
    cookie_cost = 2 * milk_cost

    # Define the number of each item
    milk_num = 1
    cereal_num = 2
    banana_num = 4
    apple_num = 4

    # Define the total cost of each item
    milk_total = milk_cost * milk_num
    cereal_total = cereal_cost * cereal_num
    banana_total = banana_cost * banana_num
    apple_total = apple_cost * apple_num

    # Define the remaining cost for cookies
    remaining_cost = 25 - milk_total - cereal_total - banana_total - apple_total

    # Calculate the number of boxes of cookies
    cookie_num = remaining_cost / cookie_cost

    result = round(cookie_num)
    return result

print(solution())