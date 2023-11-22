def solution():
    
    # Define the number of bags of 10 apples sold
    BAGS_PER_10 = 10

    # Define the total number of apples sold
    total_apples = 2000

    # Calculate the total number of bags sold
    total_bags = total_apples / BAGS_PER_10

    # Calculate the total earnings from selling the apples
    total_earnings = total_bags * 5

    # Display the total earnings
    result = total_earnings
    return result

print(solution())