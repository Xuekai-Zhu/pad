def solution():
    
    # Define the amount of money Stetson gives up per orange
    ALEC_PER_ORANGE = 10

    # Define the number of oranges picked
    oranges_picked = 60

    # Calculate the number of oranges Stetson ate
    oranges_eaten = oranges_picked * (2/5)

    # Calculate the total amount of money Stetson gave up
    total_money = oranges_eaten * ALEC_PER_ORANGE

    # Display the total amount of money Stetson gave up
    result = total_money
    return result

print(solution())