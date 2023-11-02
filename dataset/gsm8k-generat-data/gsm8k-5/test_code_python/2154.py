def solution():
    # Calculate the maximum capacity of the spacecraft in terms of people
    max_capacity = 300 * 4  # 300 family units, with 4 people per family

    # Calculate the number of people the spacecraft will carry when it leaves Earth
    initial_capacity = (max_capacity / 3) - 100

    result = initial_capacity
    return result

print(solution())