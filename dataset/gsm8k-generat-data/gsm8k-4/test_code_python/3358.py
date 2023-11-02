def solution():
    """Bob buys nose spray. He buys 10 of them for a "buy one get one free" promotion. They each cost $3. How much does he pay?"""
    # Calculate the total number of nose sprays he gets
    total_nose_sprays = 10 + (10 // 2)

    # Calculate the total cost of the nose sprays
    total_cost = total_nose_sprays * 3

    # Return the result
    result = total_cost
    return result

print(solution())