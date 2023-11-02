def solution():
    num_westward = 1800
    num_eastward = 3200
    num_north = 500

    # Calculate the number of fish caught by fishers from swimming eastward
    num_eastward_caught = 2/5 * num_eastward

    # Calculate the number of fish caught by fishers from swimming westward
    num_westward_caught = 3/4 * num_westward

    # Calculate the total number of fish caught by fishers
    total_caught = num_eastward_caught + num_westward_caught

    # Calculate the total number of fish left in the sea
    total_left = num_westward + num_eastward + num_north - total_caught
    result = total_left
    return result

print(solution())