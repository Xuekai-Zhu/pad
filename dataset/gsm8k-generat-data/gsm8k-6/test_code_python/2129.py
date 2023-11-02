def solution():
    # Calculate the total earnings from selling 5 chickens and some ducks
    earnings = 5*8 + x*10  # x is the number of ducks sold

    # Calculate the cost of the new wheelbarrow
    wheelbarrow_cost = earnings/2

    # Calculate the profit from selling the wheelbarrow
    profit = 60

    # Set up an equation to solve for the number of ducks sold
    2*wheelbarrow_cost = profit + earnings - x*10
    x = (profit + earnings - 2*wheelbarrow_cost)/10

    result = int(x)
    return result

print(solution())