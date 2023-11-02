def solution():
    """Clarissa is responsible for getting 10 copies of a manuscript printed and having each copy bound. The printers charge $0.05 per page to copy it and $5.00 per manuscript to have it bound. If the manuscript is 400 pages, how much will it cost to have it copied and bound 10 times?"""
    # Define the number of copies of the manuscript to be printed and bound
    copies = 10

    # Define the number of pages in the manuscript
    pages = 400

    # Calculate the cost of copying one manuscript
    copying_cost = pages * 0.05

    # Calculate the total cost of copying all the manuscripts
    total_copying_cost = copying_cost * copies

    # Calculate the total cost of binding all the manuscripts
    binding_cost = 5 * copies

    # Calculate the total cost of printing and binding all the manuscripts
    total_cost = total_copying_cost + binding_cost

    # return the result
    result = total_cost
    return result

print(solution())