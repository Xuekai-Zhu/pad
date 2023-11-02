def solution():
    # Define the number of jars and the capacity of each jar
    num_jars = 5
    jar_capacity = 160

    # Calculate the total number of quarters
    total_quarters = num_jars * jar_capacity

    # Calculate the total amount of money in dollars
    total_dollars = total_quarters / 4.0

    # Calculate the amount of money Jenn will have left over
    leftover_money = total_dollars - 180

    result = leftover_money
    return result

print(solution())