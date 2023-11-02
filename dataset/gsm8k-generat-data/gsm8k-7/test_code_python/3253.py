def solution():
    num_lions = 12
    num_tigers = 14

    # Calculate the total number of lions and tigers
    total_lions_and_tigers = num_lions + num_tigers

    # Calculate the number of cougars
    num_cougars = total_lions_and_tigers / 2

    # Calculate the total number of big cats
    total_big_cats = num_lions + num_tigers + num_cougars
    result = total_big_cats
    return result

print(solution())