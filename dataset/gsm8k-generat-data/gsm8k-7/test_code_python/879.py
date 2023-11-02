def solution():
    original_fortune = 80
    donated_to_charity = 20
    remaining_fortune = original_fortune - donated_to_charity
    half_to_brother = remaining_fortune / 2.0
    doubled_fortune = half_to_brother * 2.0
    tripled_fortune = doubled_fortune * 3.0
    donated_again = 10

    # Calculate the total number of coins Jake has after all transactions
    final_fortune = tripled_fortune - donated_again
    result = final_fortune
    return result

print(solution())