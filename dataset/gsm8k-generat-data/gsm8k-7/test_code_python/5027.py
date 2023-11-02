def solution():
    price_per_can = 0.25
    num_cans_at_home = 12
    num_cans_at_grandparents = 3 * num_cans_at_home
    num_cans_from_neighbor = 46
    num_cans_from_dad = 250

    # Calculate the total number of cans that Collin collected
    total_num_cans = num_cans_at_home + num_cans_at_grandparents + num_cans_from_neighbor + num_cans_from_dad

    # Calculate the total amount of money Collin can earn from the cans
    total_earnings = total_num_cans * price_per_can

    # Calculate the amount of money that Collin needs to put into savings
    amount_to_save = total_earnings / 2
    result = amount_to_save
    return result

print(solution())