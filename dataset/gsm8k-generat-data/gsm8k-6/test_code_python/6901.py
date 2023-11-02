def solution():
    # Calculate the number of friends Ron ate pizza with
    num_friends = 12 / 4  # they ordered a 12-slice pizza, and each of them ate 4 slices
    num_friends -= 1  # subtract Ron from the count of friends
    result = int(num_friends)
    return result

print(solution())