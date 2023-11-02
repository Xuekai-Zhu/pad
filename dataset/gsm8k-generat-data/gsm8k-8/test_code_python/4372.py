def solution():
    candy_cost = 49
    num_packs = 2
    starting_funds = 20

    # Calculate the total cost of the candy packs
    total_cost = candy_cost * num_packs

    # Calculate how much additional money Cory needs to buy the candy
    additional_funds = total_cost - starting_funds

    result = additional_funds
    return result

print(solution())