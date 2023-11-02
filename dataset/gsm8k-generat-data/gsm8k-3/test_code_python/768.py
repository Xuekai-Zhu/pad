def solution():
    """In her first term, Governor Sandoval gave twice as many commencement addresses as Governor Hawkins. Governor Sloan gave ten more commencement addresses than Governor Sandoval in the same amount of time. If Governor Sandoval gave 12 commencement addresses, how many commencement addresses did the three of them give altogether?"""
    # Governor Sandoval gave 12 commencement addresses
    sandoval_addresses = 12
    # Governor Hawkins gave half as many addresses as Governor Sandoval
    hawkins_addresses = sandoval_addresses / 2
    # Governor Sloan gave ten more addresses than Governor Sandoval
    sloan_addresses = sandoval_addresses + 10
    # Total number of commencement addresses given
    total_addresses = sandoval_addresses + hawkins_addresses + sloan_addresses
    result = total_addresses
    return result

print(solution())