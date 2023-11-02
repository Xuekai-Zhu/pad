def solution():
    # Calculate the number of cans Jack recycled
    total_deposit = 15  # Jack made $15
    bottles_recycled = 80
    deposit_per_bottle = 0.10
    deposit_per_can = 0.05
    deposit_from_bottles = bottles_recycled * deposit_per_bottle  # total deposit from bottles
    deposit_from_cans = (total_deposit - deposit_from_bottles) / deposit_per_can  # total number of cans
    result = deposit_from_cans
    return result

print(solution())