def solution():
    """Ray has 175 cents in nickels. Ray gives 30 cents to Peter, and he gives twice as many cents to Randi as he gave to Peter. How many more nickels does Randi have than Peter?"""
    # Define the value of a nickel in cents
    NICKEL_VALUE = 5

    # Calculate the total value of Ray's nickels in cents
    total_value = 175

    # Calculate the value of the nickels Ray gives to Peter in cents
    peter_value = 30

    # Calculate the value of the nickels Ray gives to Randi in cents
    randi_value = peter_value * 2

    # Subtract the values given to Peter and Randi from the total value to get the remaining value
    remaining_value = total_value - peter_value - randi_value

    # Calculate the number of nickels each person has based on their respective values
    peter_nickels = peter_value / NICKEL_VALUE
    randi_nickels = randi_value / NICKEL_VALUE
    remaining_nickels = remaining_value / NICKEL_VALUE

    # Calculate the difference in the number of nickels between Randi and Peter
    diff = randi_nickels - peter_nickels

    # Display the result
    result = diff
    return result

print(solution())