def solution():
    # Define initial investments
    alice_investment = 2000
    bob_investment = 2000

    # Calculate returns
    alice_return = alice_investment * 2
    bob_return = bob_investment * 5

    # Calculate final amounts
    alice_final = alice_investment + alice_return
    bob_final = bob_investment + bob_return

    # Calculate the difference
    difference = bob_final - alice_final

    result = difference
    return result

print(solution())