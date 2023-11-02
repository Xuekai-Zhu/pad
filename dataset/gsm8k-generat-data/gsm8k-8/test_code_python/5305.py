def solution():
    # Define the cost of the apple pie
    apple_pie_cost = 12

    # Calculate the cost of one cheesecake
    cheesecake_cost = apple_pie_cost / 0.75 / 3

    # Calculate the cost of the six-pack of muffins
    muffins_cost = cheesecake_cost * 2

    # Calculate the total cost of Natalie's shopping
    total_cost = 2 * cheesecake_cost + apple_pie_cost + muffins_cost

    result = total_cost
    return result

print(solution())