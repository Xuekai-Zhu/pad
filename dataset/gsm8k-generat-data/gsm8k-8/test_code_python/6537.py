def solution():
    # Define the price that Bob paid per acorn
    bob_price_per_acorn = 6000 / 3600

    # Define the total price that Alice paid
    alice_total_price = 9 * 6000

    # Calculate the price that Alice paid per acorn
    alice_price_per_acorn = alice_total_price / 3600

    result = alice_price_per_acorn
    return result

print(solution())