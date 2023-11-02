def solution():
    
    # Define Jack's initial amount of money
    jack_money = 100

    # Calculate the amount of money Sophia gave Jack
    sophia_money = jack_money * (1/5)

    # Calculate Jack's remaining amount of money
    remaining_money = jack_money - sophia_money

    # Display Jack's remaining amount of money
    result = remaining_money
    return result

print(solution())