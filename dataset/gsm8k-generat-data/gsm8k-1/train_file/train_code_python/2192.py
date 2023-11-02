def solution():
    """Niles is collecting his book club's annual fees. Each of the six members pays $150/year towards snacks, plus $30 each for six hardcover books and $12 each for six paperback books. How much money does Niles collect in total?"""
    members = 6
    snacks_fee = 150
    hardcover_fee = 30
    paperback_fee = 12
    total_fee = (snacks_fee + (hardcover_fee * 6) + (paperback_fee * 6)) * members
    result = total_fee
    return result

print(solution())