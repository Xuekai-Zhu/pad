def solution():
    """Rick held a fundraiser and is figuring out who still owes money. He marked on a sheet how much everyone has promised to contribute, but he forgot to note how much some people had actually paid. Altogether, everyone has promised to contribute $400, and Rick has actually received $285. Sally, Amy, Derek, and Carl all still owe money. Sally and Carl both owe equal amounts, Amy owes $30, and Derek owes half as much as Amy. How much, in dollars, do Sally and Carl each owe?"""
    total_promised = 400
    total_received = 285
    remaining_amount = total_promised - total_received
    amy_owes = 30
    derek_owes = amy_owes / 2
    sally_carl_owes = remaining_amount - amy_owes - derek_owes
    individual_owes = sally_carl_owes / 2
    result = individual_owes
    return result

print(solution())