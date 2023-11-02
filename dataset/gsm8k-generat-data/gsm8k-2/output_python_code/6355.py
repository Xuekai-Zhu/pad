def solution():
    """Morgan goes to the drive-thru and orders his lunch. He gets a hamburger for $4, onion rings for $2 and a smoothie for $3. If he pays with a $20 bill, how much change does he receive?"""
    total_cost = 4 + 2 + 3
    paid_amount = 20
    change = paid_amount - total_cost
    result = change
    return result

print(solution())