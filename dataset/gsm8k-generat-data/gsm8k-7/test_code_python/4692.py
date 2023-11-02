def solution():
    bag_price = 4
    monday_bags = 5
    tuesday_bags = 3
    total_money = 68

    # Calculate the total number of bags of leaves raked in the first two days
    total_bags = monday_bags + tuesday_bags

    # Calculate the total earnings from the first two days
    total_earnings = total_bags * bag_price

    # Calculate the earnings from Wednesday
    wednesday_earnings = total_money - total_earnings

    # Calculate the number of bags raked on Wednesday
    wednesday_bags = wednesday_earnings / bag_price
    result = wednesday_bags
    return result

print(solution())