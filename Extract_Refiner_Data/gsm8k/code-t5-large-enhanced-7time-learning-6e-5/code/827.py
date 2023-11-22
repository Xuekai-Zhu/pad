def solution():
    
    # Define the cost of the installation
    installation_cost = 129

    # Define the number of items installed
    mirrors = 6
    shelves = 2
    chandeliers = 2
    pictures = 20

    # Calculate the total number of items installed
    total_items = mirrors + shelves + chandeliers + pictures

    # Calculate the cost of the additional items
    additional_cost = total_items * 15

    # Calculate the total cost of the installation
    total_cost = installation_cost + additional_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())