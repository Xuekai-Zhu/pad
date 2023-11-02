def solution():
    horses = 25  # John has 25 horses
    feedings_per_day = 2  # Each horse is fed twice a day
    pounds_per_feeding = 20  # Each horse is fed 20 pounds of food per feeding
    pounds_per_bag = 1000 / 2  # Each bag contains half a ton, or 1000 pounds, of food
    days = 60  # John wants to know how many bags he'll need for 60 days

    # Calculate the total pounds of food needed in 60 days
    total_pounds = horses * feedings_per_day * pounds_per_feeding * days

    # Convert the total pounds to the number of bags needed
    bags_needed = total_pounds / pounds_per_bag
    result = bags_needed
    return result

print(solution())