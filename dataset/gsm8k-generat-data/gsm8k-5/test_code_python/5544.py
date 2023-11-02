def solution():
    total_weight = 6500  # Total weight of potatoes to be shipped
    damaged_weight = 150  # Weight of potatoes that are damaged during transport
    usable_weight = total_weight - damaged_weight  # Weight of potatoes that can be sold
    bag_weight = 50  # Weight of one bag of potatoes
    bags = usable_weight / bag_weight  # Number of bags that can be sold
    bag_price = 72  # Price of one bag of potatoes

    # Calculate the total revenue from selling the potatoes
    total_revenue = bags * bag_price
    result = total_revenue
    return result

print(solution())