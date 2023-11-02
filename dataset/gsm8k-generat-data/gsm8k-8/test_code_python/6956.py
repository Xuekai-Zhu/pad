def solution():
    shirt_cost = 80
    num_20_bills = 0
    while shirt_cost >= 20:
        num_20_bills += 1
        shirt_cost -= 20
    num_10_bills = num_20_bills - 1
    result = num_10_bills
    return result

print(solution())