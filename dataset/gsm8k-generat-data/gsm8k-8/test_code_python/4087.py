def solution():
    # Determine the total amount Mitch can spend on the boat
    total_budget = 20000 - 500 - 3*500

    # Determine the maximum length of the boat he can buy
    max_length = total_budget / 1500

    result = max_length
    return result

print(solution())