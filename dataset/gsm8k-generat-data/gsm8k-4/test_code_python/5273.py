def solution():
    """Sarah is in charge of making 2 copies of a contract for 9 people that will be in a meeting. The contract is 20 pages long. How many pages will Sarah copy?"""
    # Define the number of people and copies to be made
    num_people = 9
    num_copies = 2

    # Define the length of the contract
    contract_length = 20

    # Calculate the total number of pages to be copied
    total_pages = num_copies * contract_length * num_people

    # Return the result
    result = total_pages
    return result

print(solution())