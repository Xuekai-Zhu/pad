def solution():
    
    # Define the initial number of lollipops
    lollipops = 30

    # Subtract the number of lollipops Jean ate
    lollipops -= 2

    # Calculate the number of bags that can be filled
    bags = lollipops // 2

    # Display the number of bags that can be filled
    result = bags
    return result

print(solution())