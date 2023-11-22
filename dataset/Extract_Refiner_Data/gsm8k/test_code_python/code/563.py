def solution():
    
    # Define the initial amount of money left after the first loss
    initial_money = 5

    # Define the amount of money given for each of the next three teeth Sharon
    next_three_money = 1

    # Define the number of teeth Sharon lost
    num_next_three = 3

    # Define the number of teeth Sharon lost for each of the last two teeth Sharon
    num_last_two = 2

    # Calculate the total amount of money given for each of the previous three teeth Sharon
    previous_three_money = next_three_money * num_next_three
    previous_three_money = previous_three_money * (1/2)

    # Calculate the total amount of money given for the last two teeth Sharon
    last_two_money = last_three_money * num_last_two

    # Calculate the total amount of money given to Sharon
    total_money = initial_money

print(solution())