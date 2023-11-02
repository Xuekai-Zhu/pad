def solution():
    """Rick held a fundraiser and is figuring out who still owes money. He marked on a sheet how much everyone has promised to contribute, but he forgot to note how much some people had actually paid. Altogether, everyone has promised to contribute $400, and Rick has actually received $285.  Sally, Amy, Derek, and Carl all still owe money. Sally and Carl both owe equal amounts, Amy owes $30, and Derek owes half as much as Amy. How much, in dollars, do Sally and Carl each owe?"""
    # Define the total promised amount and the amount received
    promised = 400
    received = 285

    # Define the owed amounts for Amy and Derek
    amy_owed = 30
    derek_owed = amy_owed / 2

    # Calculate the total amount owed by Sally, Carl, and Derek
    sally_carl_derek_owed = promised - received - amy_owed - derek_owed

    # Divide the remaining owed amount equally between Sally and Carl
    sally_carl_equal_owed = sally_carl_derek_owed / 2

    # Display the amount owed by each of Sally and Carl
    result = sally_carl_equal_owed
    return result

print(solution())