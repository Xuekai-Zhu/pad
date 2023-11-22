def solution():
    
    # Define the number of cakes bought on Monday
    monday_cakes = 4

    # Define the number of cakes bought on Tuesday
    tuesday_cakes = monday_cakes * 3

    # Define the number of cakes bought on Wednesday
    wednesday_cakes = tuesday_cakes * 5

    # Calculate the total number of cakes bought
    total_cakes = monday_cakes + tuesday_cakes + wednesday_cakes

    # Display the total number of cakes bought
    result = total_cakes
    return result

print(solution())