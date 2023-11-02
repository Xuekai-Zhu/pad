def solution():
    """John has 25 horses. He feeds each horse twice a day and feeds them 20 pounds of food at each feeding. He buys half ton bags of food. How many of those will he have to buy in 60 days?"""
    # Define the number of horses, feedings per day, and pounds of food per feeding
    num_horses = 25
    feedings_per_day = 2
    pounds_per_feeding = 20

    # Calculate the total pounds of food consumed by all horses in 60 days
    total_pounds = num_horses * feedings_per_day * pounds_per_feeding * 60

    # Calculate the number of half-ton bags needed to purchase
    bags = total_pounds / (1000 / 2)

    result = round(bags)
    return result

print(solution())