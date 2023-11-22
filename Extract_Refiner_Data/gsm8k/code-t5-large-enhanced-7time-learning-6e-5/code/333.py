def solution():
    
    # Define the number of hot dogs eaten by Luke
    luke_dogs = 2

    # Define the number of hot dogs eaten by Thomas
    thomas_dogs = luke_dogs * 3

    # Define the number of hot dogs eaten by John
    john_dogs = thomas_dogs / 2

    # Calculate the difference in the number of hot dogs eaten by John and Luke
    difference = john_dogs - luke_dogs

    # Display the difference in the number of hot dogs eaten
    result = difference
    return result

print(solution())