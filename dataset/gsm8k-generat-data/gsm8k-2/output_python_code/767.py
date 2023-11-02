def solution():
    """In her first term, Governor Sandoval gave twice as many commencement addresses as Governor Hawkins. Governor Sloan gave ten more commencement addresses than Governor Sandoval in the same amount of time. If Governor Sandoval gave 12 commencement addresses, how many commencement addresses did the three of them give altogether?"""
    sandoval = 12
    hawkins = sandoval / 2
    sloan = sandoval + 10
    total = sandoval + hawkins + sloan
    result = total
    return result

print(solution())