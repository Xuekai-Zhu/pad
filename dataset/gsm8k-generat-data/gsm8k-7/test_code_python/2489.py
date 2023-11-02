def solution():
    samara_saw = 20
    friends_saw = 10
    num_friends = 3

    # Calculate the total number of alligators that Samara's friends saw
    total_friends_saw = friends_saw * num_friends

    # Calculate the total number of alligators that Samara and her friends saw
    total_saw = samara_saw + total_friends_saw
    result = total_saw
    return result

print(solution())