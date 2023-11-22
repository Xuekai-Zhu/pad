def solution():
    
    # Define the distance to the opposite inland edge
    distance = 42

    # Calculate the number of fog banks needed to cover the whole city
    num_banks = distance // 3

    # Calculate the time it takes for the fog bank to cover the whole city
    time = num_banks * 10

    # Display the time it takes for the fog bank to cover the whole city
    result = time
    return result

print(solution())