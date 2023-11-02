def solution():
    num_roses = 25
    num_tulips = 40
    num_daisies = 35

    # Calculate the total number of flowers
    total_flowers = num_roses + num_tulips + num_daisies

    # Calculate the percentage of flowers that are not roses
    percentage_not_roses = (num_tulips + num_daisies) / total_flowers * 100
    result = percentage_not_roses
    return result

print(solution())