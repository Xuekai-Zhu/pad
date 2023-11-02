def solution():
    num_copies = 10
    num_pages = 400
    copy_cost_per_page = 0.05
    bind_cost_per_copy = 5.00

    # Calculate the total cost of copying all pages for one manuscript
    copy_cost_per_manuscript = num_pages * copy_cost_per_page

    # Calculate the total cost of copying and binding one manuscript
    total_cost_per_manuscript = copy_cost_per_manuscript + bind_cost_per_copy

    # Calculate the total cost of copying and binding all manuscripts
    total_cost = total_cost_per_manuscript * num_copies
    result = total_cost
    return result

print(solution())