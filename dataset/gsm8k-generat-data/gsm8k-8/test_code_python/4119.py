def solution():
    # Define the amount of money Grant made in each of the three months
    month1 = 350
    month2 = 50 + 2*month1
    month3 = 4*(month1+month2)

    # Calculate the total amount of money Grant made in the three months
    total = month1 + month2 + month3
    result = total
    return result

print(solution())