def solution():
    num_packs_in_set = 2
    pack_size = 500 # in mL
    set_price = 2.50
    individual_price = 1.30
    num_sets = 10

    # Calculate the total cost of buying 10 sets of 2 packs
    total_set_cost = num_sets * set_price

    # Calculate the total cost of buying 20 packs individually
    total_individual_cost = (num_sets * num_packs_in_set) * (individual_price * (pack_size/1000))

    # Calculate the total savings
    total_savings = total_individual_cost - total_set_cost
    result = total_savings
    return result

print(solution())