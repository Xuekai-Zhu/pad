def solution():
    
    # Define the number of rose bushes and roses per bush
    num_bushes = 3
    roses_per_bush = 25

    # Define the number of thorns per rose
    thorns_per_rose = 8

    # Calculate the total number of roses
    total_roses = num_bushes * roses_per_bush

    # Calculate the total number of thorns
    total_thorns = total_roses * thorns_per_rose

    # return the result
    result = total_thorns
    return result

print(solution())