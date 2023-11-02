def solution():
    """ Bruno wants to buy two and one-half dozens of pens. How many pens will he have? """
    # Define the number of pens in one dozen
    PENS_PER_DOZEN = 12

    # Define the number of dozens of pens Bruno wants to buy
    dozens = 2.5

    # Calculate the total number of pens Bruno will have
    pens = PENS_PER_DOZEN * dozens

    # Display the total number of pens
    result = pens
    return result

print(solution())