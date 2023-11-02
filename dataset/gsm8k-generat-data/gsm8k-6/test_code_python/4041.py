def solution():
    # Calculate the number of oranges given to the brother
    given_to_brother = 12/3  

    # Calculate the remaining number of oranges
    remaining_oranges = 12 - given_to_brother  

    # Calculate the number of oranges given to the friend
    given_to_friend = remaining_oranges/4  
    result = given_to_friend
    return result

print(solution())