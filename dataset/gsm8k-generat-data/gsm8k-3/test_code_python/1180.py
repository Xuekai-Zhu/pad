def solution():
    """A local restaurant is offering an 8 piece fried chicken bucket and 2 sides for $12.00 that will feed 6 people.  If Monty was having a family reunion for 36 family members, how much will it cost him to buy enough chicken and sides to feed everyone one serving?"""
    # Define the cost of 1 bucket with 2 sides
    BUCKET_PRICE = 12

    # Calculate the number of servings needed
    servings_needed = 36

    # Calculate the number of buckets needed, rounding up to the nearest whole number
    buckets_needed = math.ceil(servings_needed / 6)

    # Calculate the total cost of the buckets
    total_cost = buckets_needed * BUCKET_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())