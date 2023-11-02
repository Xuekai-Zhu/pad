def solution():
    """A pencil costs $0.5 each and a folder costs $0.9 each. An office needs two dozen pencils and 20 pieces of folders. How much does it cost to buy the office supplies?"""
    pencil_cost = 0.5
    folder_cost = 0.9
    pencils_needed = 24
    folders_needed = 20
    total_cost = (pencil_cost * pencils_needed) + (folder_cost * folders_needed)
    result = total_cost
    return result

print(solution())