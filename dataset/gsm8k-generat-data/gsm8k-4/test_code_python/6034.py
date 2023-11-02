def solution():
    """Brenden went fishing with his dad. Brenden caught 8 fish in the morning. He threw 3 back that were too small. He caught 5 more in the afternoon. Brendan’s dad caught 13 fish. How many fish did they catch in all?"""
    # Brendan caught 8 fish in the morning and threw 3 back, so he has 8 - 3 = 5 fish.
    brenden_fish = 5

    # Brendan caught 5 more fish in the afternoon, so he has a total of 5 + 5 = 10 fish.
    brenden_fish += 5

    # Brendan and his dad caught a total of 10 + 13 = 23 fish.
    total_fish = brenden_fish + 13

    result = total_fish
    return result

print(solution())