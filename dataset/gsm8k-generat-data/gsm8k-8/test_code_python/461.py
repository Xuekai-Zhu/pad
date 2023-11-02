def solution():
    # Define the number of manuscripts and the number of pages per manuscript
    num_copies = 10
    num_pages = 400

    # Calculate the cost of printing and binding one manuscript
    cost_per_copy = (num_pages * 0.05) + 5.00

    # Calculate the total cost of printing and binding all manuscripts
    total_cost = num_copies * cost_per_copy
    result = total_cost
    return result

print(solution())