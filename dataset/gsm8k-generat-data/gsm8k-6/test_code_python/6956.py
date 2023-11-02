def solution():
    # Let x be the number of $10 bills
    x = 0
    while True:
        # Calculate the total amount of money in $10 and $20 bills
        total_amount = 10*x + 20*(x+1)  

        # Check if the total amount is equal to $80
        if total_amount == 80:
            result = x
            break

        # If the total amount is greater than $80, there is no solution
        elif total_amount > 80:
            result = "No solution"
            break

        # If the total amount is less than $80, increment the number of $10 bills and try again
        else:
            x += 1

    return result

print(solution())