def solution():
    
    # Define Ronnie's initial amount of money
    ronnie_money = 5

    # Define Rissa's initial amount of money
    rissa_money = ronnie_money * 3

    # Calculate how much money Rissa has left after each of them given an equal amount to their little sister
    left_after_each = (4/5) * rissa_money

    # Calculate how much money is left in Ronnie's money
    left_after_each = left_after_each - rissa_money

    # Display how much is left in Ronnie's money
    result = left_after_each
    return result

print(solution())