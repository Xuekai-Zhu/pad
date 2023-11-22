def solution():
    
    # Define the initial number of apples
    initial_apples = 60

    # Calculate the number of apples Walter ate
    walter_apples = initial_apples * (2/5)

    # Calculate the number of apples remaining after Walter ate
    remaining_apples = initial_apples - walter_apples

    # Calculate the number of apples Walter gave to his sister
    sister_apples = remaining_apples * 0.25

    # Calculate the number of apples Walter received from selling to his uncle
    sold_apples = remaining_apples - sister_apples

    # Calculate the total amount of money Walter received
    total_money = sold_apples * 3

    # Display the total amount of money Walter received
    result = total_money
    return result

print(solution())