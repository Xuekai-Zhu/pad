def solution():
    # Let x be the total number of chocolates in the box
    x = 0.5*x + 0.5*x  # Half have nuts and half do not
    x *= (1-0.8) + 0.5*(1-0.5)  # Students eat 80% of chocolates with nuts and half of chocolates without nuts
    remaining_chocolates = 28  # There are 28 chocolates left
    total_chocolates = remaining_chocolates / (1 - ((1-0.8) + 0.5*(1-0.5)))  # Solve for x

    result = total_chocolates
    return result

print(solution())