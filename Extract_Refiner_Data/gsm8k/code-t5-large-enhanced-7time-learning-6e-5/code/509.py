def solution():
    
    # Define the initial amount of money Julie had
    initial_money = 500

    # Calculate the amount spent on clothes
    clothes_cost = initial_money * 0.2

    # Calculate the remaining money after clothes
    remaining_money = initial_money - clothes_cost

    # Calculate the amount spent on CDs
    cd_cost = remaining_money * 0.25

    # Calculate the final amount of money Julie has left
    final_money = remaining_money - cd_cost

    # Display the final amount of money Julie has left
    result = final_money
    return result

print(solution())