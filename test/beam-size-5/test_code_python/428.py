def solution():
    
    # Define the number of dragons Prince Thaddeus slew
    thaddeus_dragons = 100

    # Calculate the number of dragons Prince Arthur slew
    arthur_dragons = thaddeus_dragons * 0.75

    # Calculate the number of dragons Prince Walter slew
    walter_dragons = arthur_dragons * 2

    # Calculate the number of dragons Prince Bruce slew
    bruce_dragons = walter_dragons / 5

    # Calculate the total number of dragons
    total_dragons = thaddeus_dragons + arthur_dragons + walter_dragons + bruce_dragons

    # Display the total number of dragons
    result = total_dragons
    return result

print(solution())