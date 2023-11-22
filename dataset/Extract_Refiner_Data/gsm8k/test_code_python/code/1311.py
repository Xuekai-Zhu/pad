def solution():
    
    # Define the time it takes to peel an orange and Jane
    ana_time = 3
    jane_time = 4

    # Calculate the number of oranges Ana and Jane will pick in an hour
    ana_oranges = (ana_time + jane_time) * 60
    jane_oranges = (jane_time * 60) * 60

    # Calculate the difference in the number of oranges Ana and Jane will peel
    difference = ana_oranges - jane_oranges

    # Display the difference in the number of oranges Ana and Jane will peel
    result = difference
    return result

print(solution())