def solution():
    """In her first term, Governor Sandoval gave twice as many commencement addresses as Governor Hawkins.
    Governor Sloan gave ten more commencement addresses than Governor Sandoval in the same amount of time.
    If Governor Sandoval gave 12 commencement addresses, how many commencement addresses did the three of them give altogether?"""
    
    # Find the number of commencement addresses Governor Hawkins gave
    sandoval_addresses = 12
    hawkins_addresses = sandoval_addresses / 2

    # Find the number of commencement addresses Governor Sloan gave
    sloan_addresses = sandoval_addresses + 10

    # Find the total number of commencement addresses given by all three governors
    total_addresses = sandoval_addresses + hawkins_addresses + sloan_addresses

    result = total_addresses
    return result

print(solution())