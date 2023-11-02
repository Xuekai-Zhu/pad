def solution():
    # Calculate the total cost of Carrie's clothes
    shirt_cost = 4 * 8
    pants_cost = 2 * 18
    jacket_cost = 2 * 60
    total_cost = shirt_cost + pants_cost + jacket_cost

    # Calculate how much Carrie's mom pays
    mom_payment = total_cost / 2

    # Calculate how much Carrie pays
    carrie_payment = total_cost - mom_payment
    result = carrie_payment
    return result

print(solution())