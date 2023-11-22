def solution():
    
    # Define the amount of yarn in a skein
    YARN_PER_SKIN = 364

    # Calculate the amount of yarn used by Mariah's grandma
    mariah_yarn = YARN_PER_SKIN / 4

    # Calculate the amount of yarn used by the grandma
    grandma_yarn = YARN_PER_SKIN / 2

    # Calculate the total amount of yarn used
    total_yarn = mariah_yarn + grandma_yarn

    # Display the total amount of yarn used
    result = total_yarn
    return result

print(solution())