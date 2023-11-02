def solution():
    num_kids = 4
    ears_per_row = 70
    seeds_per_bag = 48
    seeds_per_ear = 2
    pay_per_row = 1.5
    dinner_cost_per_kid = 36

    # Calculate the total number of ears of corn that need to be planted
    total_ears = num_kids * ears_per_row

    # Calculate the total number of seeds needed
    total_seeds = total_ears * seeds_per_ear

    # Calculate the total number of bags of seeds needed
    total_bags = total_seeds / seeds_per_bag

    # Calculate the total amount earned by the kids
    total_pay = num_kids * pay_per_row

    # Calculate the amount spent on dinner by each kid
    dinner_cost_per_kid = dinner_cost_per_kid / 2

    # Calculate the amount each kid spent on seeds
    amount_spent_on_seeds = total_pay - dinner_cost_per_kid

    # Calculate the number of bags of seeds each kid used
    bags_per_kid = amount_spent_on_seeds / num_kids / seeds_per_bag

    result = bags_per_kid
    return result

print(solution())