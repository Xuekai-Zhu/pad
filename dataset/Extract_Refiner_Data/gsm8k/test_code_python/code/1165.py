def solution():
    
    # Define the initial amount of money given by Ronnie and Rissa
    ronnie_money = 5
    rissa_money = 3 * ronnie_money

    # Calculate the total amount of money given to Ronnie and Rissa
    total_money = ronnie_money + rissa_money

    # Calculate the amount of money left after each person gets their share
    remaining_money = total_money - (4/5) * total_money

    # Display the amount of money left in Ronnie's money
    result = remaining_money
    return result

print(solution())