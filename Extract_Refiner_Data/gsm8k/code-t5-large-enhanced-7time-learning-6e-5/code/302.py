def solution():
    
    # Define the total number of loaves produced each day
    total_loaves = 60

    # Calculate the number of loaves sold in the morning
    morning_sales = total_loaves * (2/3)

    # Calculate the number of loaves left after morning sales
    remaining_loaves = total_loaves - morning_sales

    # Calculate the number of loaves sold in the afternoon and evening
    afternoon_sales = remaining_loaves * (1/2)

    # Display the number of loaves sold in the afternoon
    result = afternoon_sales
    return result

print(solution())