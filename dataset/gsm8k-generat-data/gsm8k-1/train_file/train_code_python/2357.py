def solution():
    """A pencil costs $0.5 each and a folder costs $0.9 each. An office needs two dozen pencils and 20 pieces of folders. How much does it cost to buy the office supplies?"""
    pencils_price = 0.5
    folders_price = 0.9
    pencils_per_dozen = 12
    pencils_needed = 2 * pencils_per_dozen
    folders_needed = 20
    total_cost = (pencils_needed * pencils_price) + (folders_needed * folders_price)
    result = total_cost
    return result

print(solution())