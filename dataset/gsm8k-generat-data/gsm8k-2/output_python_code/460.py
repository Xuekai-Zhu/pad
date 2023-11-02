def solution():
    """Clarissa is responsible for getting 10 copies of a manuscript printed and having each copy bound.
    The printers charge $0.05 per page to copy it and $5.00 per manuscript to have it bound.
    If the manuscript is 400 pages, how much will it cost to have it copied and bound 10 times?"""
    manuscript_pages = 400
    num_copies = 10
    copy_cost = manuscript_pages * 0.05
    bound_cost = 5.00
    total_cost = (copy_cost + bound_cost) * num_copies
    result = total_cost
    return result

print(solution())