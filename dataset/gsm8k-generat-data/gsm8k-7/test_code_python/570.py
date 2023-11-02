def solution():
    num_dimes = 5
    num_quarters = 3
    num_nickels = 8
    num_pennies = 60

    # Calculate the total amount of money in cents that Cindy put in the pond
    cindy_total = num_dimes * 10

    # Calculate the total amount of money in cents that Eric put in the pond
    eric_total = num_quarters * 25

    # Calculate the total amount of money in cents that Garrick put in the pond
    garrick_total = num_nickels * 5

    # Calculate the total amount of money in cents that Ivy put in the pond
    ivy_total = num_pennies * 1

    # Calculate the total amount of money in cents that they put in the pond
    total = cindy_total + eric_total + garrick_total + ivy_total
    result = total
    return result

print(solution())