def solution():
    num_potatoes = 80
    sold_to_adams = 20
    sold_to_lenon = 15

    # Calculate the total number of sweet potatoes sold
    total_sold = sold_to_adams + sold_to_lenon

    # Calculate the number of sweet potatoes that are not yet sold
    num_unsold = num_potatoes - total_sold
    result = num_unsold
    return result

print(solution())