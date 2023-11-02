def solution():
    """A pencil costs $0.5 each and a folder costs $0.9 each. An office needs two dozen pencils and 20 pieces of folders. How much does it cost to buy the office supplies?"""
    # Define the cost of a pencil and a folder
    PENCIL_PRICE = 0.5
    FOLDER_PRICE = 0.9

    # Define the number of pencils and folders needed
    pencils_needed = 2 * 12
    folders_needed = 20

    # Calculate the total cost of the pencils
    pencil_cost = pencils_needed * PENCIL_PRICE

    # Calculate the total cost of the folders
    folder_cost = folders_needed * FOLDER_PRICE

    # Calculate the total cost of all the supplies
    total_cost = pencil_cost + folder_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())