def solution():
    # Find the total amount paid by Alice
    alice_total_paid = 9 * 6000
    # Divide the total paid by the number of acorns to find the price per acorn
    price_per_acorn = alice_total_paid / 3600
    result = price_per_acorn
    return result

print(solution())