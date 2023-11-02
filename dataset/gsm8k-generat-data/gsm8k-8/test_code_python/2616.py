def solution():
    # Define the number of bottles Don buys from Shop A and Shop B
    a = 150
    b = 180

    # Calculate the number of bottles Don needs to buy from Shop C to reach his limit of 550 bottles
    c = 550 - (a + b)

    result = c
    return result

print(solution())