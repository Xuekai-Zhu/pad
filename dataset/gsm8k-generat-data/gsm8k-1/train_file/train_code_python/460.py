def solution():
    """Clarissa is responsible for getting 10 copies of a manuscript printed and having each copy bound. The printers charge $0.05 per page to copy it and $5.00 per manuscript to have it bound. If the manuscript is 400 pages, how much will it cost to have it copied and bound 10 times?"""
    pages = 400
    copies = 10
    cost_per_page = 0.05
    cost_per_manuscript = 5.00
    total_pages = pages * copies
    copying_cost = total_pages * cost_per_page
    binding_cost = copies * cost_per_manuscript
    total_cost = copying_cost + binding_cost
    result = total_cost
    return result

print(solution())