def solution():
    
    # Define the amount of money each person had
    each_money = 60

    # Calculate the amount of money Maggie spent
    maggie_spent = each_money / 4

    # Calculate the amount of money Riza spent
    riza_spent = each_money / 3

    # Calculate the total amount of money the two of them have
    total_money = maggie_spent + riza_spent

    # Calculate the amount of money the two of them have left
    money_left = total_money - total_money

    # Display the amount of money the two of them have left
    result = money_left
    return result

print(solution())