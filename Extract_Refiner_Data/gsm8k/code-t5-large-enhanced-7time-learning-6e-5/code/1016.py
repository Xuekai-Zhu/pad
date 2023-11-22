def solution():
    
    # Define the number of bananas picked on Wednesday
    wednesday_bananas = 4

    # Define the number of bananas picked on Thursday
    thursday_bananas = 6

    # Define the number of bananas picked on Friday
    friday_bananas = wednesday_bananas * 3

    # Calculate the total number of bananas picked
    total_bananas = wednesday_bananas + thursday_bananas + friday_bananas

    # Display the total number of bananas
    result = total_bananas
    return result

print(solution())