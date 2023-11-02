def solution():
    """1,800 fish swim westward, 3,200 swim eastward, and 500 swim north. What is the number of fish left in the sea, if fishers catch 2/5 of the fish that swam eastward and 3/4 of the fish that swam westward?"""
    # Calculate the number of fish caught by the fishers
    eastward_catch = 3/5 * 3200
    westward_catch = 3/4 * 1800

    # Calculate the total number of fish remaining
    total_remaining = 1800 - westward_catch + 3200 - eastward_catch + 500

    # Return the result
    result = total_remaining
    return result

print(solution())