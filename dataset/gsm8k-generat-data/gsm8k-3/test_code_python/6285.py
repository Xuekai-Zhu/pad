def solution():
    """Maggie went to Lou's aquarium and saw 100 goldfish in the aquarium. She asked if she could take some home to care for, and she was allowed to catch half of them. While using a catching net, she caught 3/5 of the total number of goldfish she was allowed to take home. How many goldfish does Maggie remain with to catch to get the total number she was allowed to take home?"""
    # Calculate the number of goldfish Maggie is allowed to take home
    allowed_num = 100 / 2

    # Calculate the number of goldfish Maggie has already caught
    caught_num = allowed_num * 3 / 5

    # Calculate the remaining number of goldfish Maggie needs to catch
    remaining_num = allowed_num - caught_num

    # Display the remaining number of goldfish Maggie needs to catch
    result = remaining_num
    return result

print(solution())