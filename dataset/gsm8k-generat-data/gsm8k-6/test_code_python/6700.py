def solution():
    # Calculate the cost per ounce for each bottle of ketchup
    ketchup_10 = 1 / 10        # Cost per ounce of the 10-ounce bottle
    ketchup_16 = 2 / 16        # Cost per ounce of the 16-ounce bottle
    ketchup_25 = 2.5 / 25      # Cost per ounce of the 25-ounce bottle
    ketchup_50 = 5 / 50        # Cost per ounce of the 50-ounce bottle
    ketchup_200 = 10 / 200    # Cost per ounce of the 200-ounce bottle

    # Calculate how many bottles of ketchup Billy can buy with his $10
    total_cost = 0
    num_bottles = 0

    # Try purchasing the $10 bottle first
    if ketchup_200 <= 10:
        total_cost += 10
        num_bottles += 1

    # Try purchasing the $5 bottle next
    if ketchup_50 <= 10 - total_cost:
        total_cost += ketchup_50 * 50
        num_bottles += 1

    # Try purchasing the 25-ounce bottle next
    if ketchup_25 <= 10 - total_cost:
        total_cost += ketchup_25 * 25
        num_bottles += 1

    # Try purchasing the 16-ounce bottle next
    if ketchup_16 <= 10 - total_cost:
        total_cost += ketchup_16 * 16
        num_bottles += 1

    # Purchase as many of the 10-ounce bottles as he can afford with the remaining money
    while ketchup_10 <= 10 - total_cost:
        total_cost += ketchup_10 * 10
        num_bottles += 1

    result = num_bottles
    return result

print(solution())