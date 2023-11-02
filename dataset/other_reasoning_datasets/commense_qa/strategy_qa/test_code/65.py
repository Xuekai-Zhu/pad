def solution():
    library_product_list = ["books", "DVDs", "magazines", "audiobooks"]
    alpo_product_list = ["pet food", "pet toys", "pet grooming products"]
    overlap = [product for product in library_product_list if product in alpo_product_list]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())