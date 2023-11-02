def solution():
    copies = 2  # Sarah needs to make 2 copies of the contract
    people = 9  # There will be 9 people in the meeting
    pages_per_copy = 20  # The contract is 20 pages long

    # Calculate the total number of pages Sarah will need to copy
    total_pages = copies * people * pages_per_copy
    result = total_pages
    return result

print(solution())