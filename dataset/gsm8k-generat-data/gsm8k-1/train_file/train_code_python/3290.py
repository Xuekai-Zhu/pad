def solution():
    """Rick held a fundraiser and is figuring out who still owes money. He marked on a sheet how much everyone has promised to contribute, but he forgot to note how much some people had actually paid. Altogether, everyone has promised to contribute $400, and Rick has actually received $285. Sally, Amy, Derek, and Carl all still owe money. Sally and Carl both owe equal amounts, Amy owes $30, and Derek owes half as much as Amy. How much, in dollars, do Sally and Carl each owe?"""
    total_promised = 400
    total_received = 285
    sally_carl_share = (total_promised - total_received - 30 - (0.5*30))/2
    result = sally_carl_share
    return result

print(solution())