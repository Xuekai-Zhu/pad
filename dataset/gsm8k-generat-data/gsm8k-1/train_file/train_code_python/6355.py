def solution():
    """Morgan goes to the drive-thru and orders his lunch. He gets a hamburger for $4, onion rings for $2 and a smoothie for $3. If he pays with a $20 bill, how much change does he receive?"""
    hamburger_price = 4
    onion_rings_price = 2
    smoothie_price = 3
    total_price = hamburger_price + onion_rings_price + smoothie_price
    bill_paid = 20
    change = bill_paid - total_price
    result = change
    return result

print(solution())