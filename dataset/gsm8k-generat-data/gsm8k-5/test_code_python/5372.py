def solution():
    boxes_of_tissues = 10  # Annalise needs to buy 10 boxes of tissues
    packs_per_box = 20  # Each box has 20 packs of tissues
    tissues_per_pack = 100  # Each pack contains 100 tissues
    price_per_tissue = 0.05  # Each tissue costs 5 cents

    # Calculate the total number of tissues Annalise will buy
    total_tissues = boxes_of_tissues * packs_per_box * tissues_per_pack

    # Calculate the total cost of the tissues
    total_cost = total_tissues * price_per_tissue
    result = total_cost
    return result

print(solution())