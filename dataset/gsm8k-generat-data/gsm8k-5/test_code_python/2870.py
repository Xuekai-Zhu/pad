def solution():
    total_money = 300  # Hanna has $300
    cost_per_rose = 2  # Each rose costs $2
    num_roses = total_money // cost_per_rose  # Hanna can buy the maximum number of roses within her budget

    # Calculate the number of roses for each friend
    roses_for_jenna = num_roses // 3
    roses_for_imma = num_roses // 2

    # Calculate the total number of roses for both friends
    total_roses = roses_for_jenna + roses_for_imma
    result = total_roses
    return result

print(solution())