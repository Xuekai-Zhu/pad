def solution():
    
    # Define the initial number of shoes
    shoes = 200

    # Calculate the number of shoes after Monday
    shoes -= 5

    # Calculate the number of shoes after Wednesday
    shoes += 15

    # Calculate the number of shoes after Friday
    shoes += 30

    # Calculate the number of shoes after Saturday
    shoes -= 180

    # Display the number of shoes on Sunday
    result = shoes
    return result

print(solution())