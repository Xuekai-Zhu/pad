def solution():
    num_tulips = 250
    tulip_cost = 2

    num_carnations = 375
    carnation_cost = 2

    num_roses = 320
    rose_cost = 2

    # Calculate the total cost of all tulips
    total_tulip_cost = num_tulips * tulip_cost

    # Calculate the total cost of all carnations
    total_carnation_cost = num_carnations * carnation_cost

    # Calculate the total cost of all roses
    total_rose_cost = num_roses * rose_cost

    # Calculate the total cost of all flowers
    total_cost = total_tulip_cost + total_carnation_cost + total_rose_cost
    result = total_cost
    return result

print(solution())