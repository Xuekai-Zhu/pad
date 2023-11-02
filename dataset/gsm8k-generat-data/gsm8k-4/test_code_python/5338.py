def solution():
    """Rick can iron 4 dress shirts in an hour. He can iron 3 dress pants in an hour. If he spends 3 hours ironing dress shirts and 5 hours ironing dress pants, how many pieces of clothing has he ironed?"""
    # Define the rate of ironing for dress shirts and dress pants
    shirts_rate = 4
    pants_rate = 3

    # Calculate the total number of dress shirts ironed
    shirts_total = shirts_rate * 3

    # Calculate the total number of dress pants ironed
    pants_total = pants_rate * 5

    # Calculate the total number of pieces of clothing ironed
    total = shirts_total + pants_total

    # return the result
    result = total
    return result

print(solution())