def solution():
    num_dozen_macarons = 3
    num_additional_macarons = 10
    num_left_over_macarons = 15

    # Calculate the total number of macarons Emma bought
    total_macarons = (num_dozen_macarons * 12) + num_additional_macarons

    # Calculate the number of macarons eaten
    num_macarons_eaten = total_macarons - num_left_over_macarons
    result = num_macarons_eaten
    return result

print(solution())