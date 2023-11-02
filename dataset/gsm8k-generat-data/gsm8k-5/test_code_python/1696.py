def solution():
    total_bill = 150  # The total dinner bill is $150
    silas_share = total_bill / 2  # Silas will pay half of the bill
    remaining_share = (total_bill - silas_share) * 1.1  # The remaining friends will split the rest of the bill and add a 10% tip

    # Calculate the amount each of the remaining friends will pay
    num_remaining_friends = 6 - 1  # There are 6 friends in total, but Silas is paying for half of the bill
    per_friend_share = remaining_share / num_remaining_friends
    result = per_friend_share
    return result

print(solution())