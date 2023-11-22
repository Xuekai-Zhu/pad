def solution():
    
    # Define the initial number of candies George has
    george_candies = 3

    # Calculate the number of candies Nick had
    nick_candies = george_candies * 2

    # Calculate the number of candies Nick has after George ate 5
    nick_candies += 5

    # Display the number of candies Nick has
    result = nick_candies
    return result

print(solution())