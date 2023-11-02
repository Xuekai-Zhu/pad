def solution():
    """Clarissa is responsible for getting 10 copies of a manuscript printed and having each copy bound.  The printers charge $0.05 per page to copy it and $5.00 per manuscript to have it bound.  If the manuscript is 400 pages, how much will it cost to have it copied and bound 10 times?"""
    # Define the cost per page and per manuscript
    COPY_PRICE = 0.05
    BINDING_PRICE = 5.00

    # Define the number of copies needed and the number of pages in the manuscript
    NUM_COPIES = 10
    NUM_PAGES = 400

    # Calculate the total cost of copying all the pages
    copy_cost = NUM_COPIES * NUM_PAGES * COPY_PRICE

    # Calculate the total cost of binding all the copies
    binding_cost = NUM_COPIES * BINDING_PRICE

    # Calculate the total cost of printing and binding
    total_cost = copy_cost + binding_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())