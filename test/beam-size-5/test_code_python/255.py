def solution():
    
    # Define the number of apples Andrea has
    andrea_apples = 52

    # Calculate the number of apples Jamal has
    jamal_apples = andrea_apples + 8

    # Calculate the number of bananas Jamal has
    jamal_bananas = jamal_apples / 2

    # Calculate the number of apples Jamal has
    jamal_apples = jamal_apples + 4

    # Calculate the total number of fruits
    total_fruits = andrea_apples + jamal_bananas + jamal_apples

    # Display the total number of fruits
    result = total_fruits
    return result

print(solution())