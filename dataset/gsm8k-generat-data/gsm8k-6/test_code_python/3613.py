def solution():
    # Calculate the balance of Pam's bank account at the beginning of the year
    final_balance = 950  # current balance
    amount_withdrawn = 250  # amount withdrawn at the end of the year
    starting_balance = final_balance - amount_withdrawn  # balance before withdrawal
    starting_balance /= 3  # balance tripled during the year
    result = starting_balance
    return result

print(solution())