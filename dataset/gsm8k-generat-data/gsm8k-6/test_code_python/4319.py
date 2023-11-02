def solution():
    # Calculate the total number of oranges Tammy can pick in 3 weeks
    total_oranges = 10 * 12 * 21  # 10 trees, 12 oranges per tree per day, 21 days in 3 weeks

    # Calculate the number of 6-packs Tammy can make
    num_six_packs = total_oranges // 6

    # Calculate the amount of money Tammy can earn
    earnings = num_six_packs * 2

    result = earnings
    return result

print(solution())