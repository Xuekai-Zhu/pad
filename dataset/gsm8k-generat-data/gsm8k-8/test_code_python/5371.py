def solution():
    # Define the number of apples Martha has
    total_apples = 20

    # Calculate how many apples Jane got
    jane_apples = 5

    # Calculate how many apples James got
    james_apples = jane_apples + 2

    # Subtract the apples given to Jane and James
    remaining_apples = total_apples - jane_apples - james_apples

    # Calculate how many more apples Martha needs to give away
    extra_apples = remaining_apples - 4
    result = extra_apples
    return result

print(solution())