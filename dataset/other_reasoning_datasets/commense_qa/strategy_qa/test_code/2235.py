def solution():
    leopard_cat_status = "Least Concern"
    bornean_orangutan_status = "Endangered"
    if leopard_cat_status < bornean_orangutan_status:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())