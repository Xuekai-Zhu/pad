def solution():
    """Sarah is in charge of making 2 copies of a contract for 9 people that will be in a meeting.  The contract is 20 pages long.  How many pages will Sarah copy?"""
    # Define the number of copies and the number of people in the meeting
    num_copies = 2
    num_people = 9

    # Define the length of the contract in pages
    contract_length = 20

    # Calculate the total number of pages that Sarah will copy
    total_pages = num_copies * contract_length * num_people

    # Display the total number of pages
    result = total_pages
    return result

print(solution())