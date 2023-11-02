def solution():
    pages = 400  # The manuscript is 400 pages long
    copies = 10  # Clarissa needs to get 10 copies printed and bound
    copy_cost = 0.05 * pages  # The cost to copy one page is $0.05
    bind_cost = 5  # The cost to bind one manuscript is $5.00

    # Calculate the total cost to print and bind 10 copies of the manuscript
    total_cost = (copy_cost + bind_cost) * copies
    result = total_cost
    return result

print(solution())