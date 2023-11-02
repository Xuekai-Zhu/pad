def solution():
    # Calculate the total bananas collected in piles with 9 hands
    bananas_9hands = 6 * 9 * 14

    # Calculate the total bananas collected in piles with 12 hands
    bananas_12hands = 4 * 12 * 9

    # Calculate the total bananas collected
    total_bananas = bananas_9hands + bananas_12hands

    # Calculate the number of bananas each monkey gets if they divide equally
    bananas_per_monkey = total_bananas / 12

    result = bananas_per_monkey
    return result

print(solution())