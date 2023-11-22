def solution():
    
    # Calculate the cost of the first 10 boards
    board1_cost = 10 * 2 * 4 * 10

    # Calculate the cost of the remaining 10 boards
    board2_cost = 10 * 2 * 4 * 10

    # Calculate the total cost of the boards
    total_cost = board1_cost + board2_cost

    # Calculate the cost of the remaining 10 boards
    board3_cost = 10 * 4 * 10

    # Calculate the total revenue from selling the boards
    total_revenue = board3_cost + board4_cost

    # Calculate the profit
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())