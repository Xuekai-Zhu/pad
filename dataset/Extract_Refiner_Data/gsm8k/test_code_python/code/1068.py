def solution():
    
    # Define the initial amount of money each person had
    initial_money = 60

    # Calculate the amount of money Maggie spent
    maggie_spent = initial_money / 4

    # Calculate the amount of money Riza spent
    riza_spent = initial_money / 3

    # Calculate the total amount of money they have left
    total_left = initial_money - maggie_spent - riza_spent

    # Display the total amount of money they have left
    result = total_left
    return result

print(solution())