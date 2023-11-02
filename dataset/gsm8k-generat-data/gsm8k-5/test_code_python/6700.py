def solution():
    # Initialize the bottles and prices
    bottles = []
    prices = []

    # Calculate the price per ounce for each bottle and append it to the prices list
    prices.append(1/10)  # $1 for 10 ounces
    prices.append(2/16)  # $2 for 16 ounces
    prices.append(2.5/25)  # $2.5 for 25 ounces
    prices.append(5/50)  # $5 for 50 ounces
    prices.append(10/200)  # $10 for 200 ounces

    # Sort the prices list in ascending order
    prices.sort()

    # Initialize the total ounces and number of bottles bought
    total_ounces = 0
    num_bottles = 0

    # Loop through the prices list starting from the cheapest
    for price in prices:
        # Calculate the number of ounces in the bottle
        ounces = price*10
        # If the total ounces plus the ounces in the bottle is less than or equal to 100, buy the bottle
        if total_ounces + ounces <= 100:
            total_ounces += ounces
            num_bottles += 1
        # If the total ounces is greater than or equal to 100, stop buying bottles
        else:
            break

    result = num_bottles
    return result

print(solution())