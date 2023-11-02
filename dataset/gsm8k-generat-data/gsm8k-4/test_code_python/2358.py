def solution():
    """A pencil costs $0.5 each and a folder costs $0.9 each. An office needs two dozen pencils and 20 pieces of folders. How much does it cost to buy the office supplies?"""
    # Define the prices and quantities of pencils and folders
    pencil_price = 0.5
    folder_price = 0.9
    num_pencils = 2 * 12
    num_folders = 20

    # Calculate the total cost of the office supplies
    total_cost = (pencil_price * num_pencils) + (folder_price * num_folders)

    # return the result
    result = total_cost
    return result

print(solution())