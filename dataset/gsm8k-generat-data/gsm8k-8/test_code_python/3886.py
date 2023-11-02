def solution():
    # Define the number of tent stakes as x
    x = 1

    # Calculate the number of drink mix packets (3 times the number of tent stakes)
    drink_mix = 3 * x

    # Calculate the number of bottles of water (2 more than the number of tent stakes)
    water = x + 2

    # Calculate the total number of items (sum of tent stakes, drink mix packets, and water bottles)
    total_items = x + drink_mix + water

    # Use trial and error to find the value of x that results in a total of 22 items
    while total_items != 22:
        x += 1
        drink_mix = 3 * x
        water = x + 2
        total_items = x + drink_mix + water

    result = x
    return result

print(solution())