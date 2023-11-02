def solution():
    aldi_charges_for_paper_bags = True
    aldi_requires_deposit_for_shopping_carts = True
    if aldi_charges_for_paper_bags and aldi_requires_deposit_for_shopping_carts:
        result = "yes, it is recommended to bring your own bags to Aldi"
    else:
        result = "no, it is not necessary to bring your own bags to Aldi"
    return result

print(solution())