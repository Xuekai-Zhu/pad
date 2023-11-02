def solution():
    trees = 10  # Tammy has 10 orange trees
    oranges_per_day = 12  # Tammy can pick 12 oranges from each tree per day
    packs_per_orange = 1/6  # Tammy sells oranges in 6-packs, so there are 1/6 of an orange per pack
    price_per_pack = 2  # Tammy sells each 6-pack for $2
    days_per_week = 7  # There are 7 days in a week
    weeks = 3  # Tammy wants to know how much money she will make in 3 weeks

    # Calculate the total number of oranges Tammy can pick in 3 weeks
    total_oranges = trees * oranges_per_day * days_per_week * weeks

    # Calculate the total number of 6-packs Tammy can sell
    total_packs = total_oranges * packs_per_orange

    # Calculate the total amount of money Tammy will earn
    total_money = total_packs * price_per_pack
    result = total_money
    return result

print(solution())