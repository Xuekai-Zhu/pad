def solution():
    num_cans_of_soup = 6
    soup_price = 2
    num_loaves_of_bread = 2
    bread_price = 5
    num_boxes_of_cereal = 2
    cereal_price = 3
    num_gallons_of_milk = 2
    milk_price = 4

    # Calculate the total cost of all groceries
    total_cost = (num_cans_of_soup * soup_price) + (num_loaves_of_bread * bread_price) + (num_boxes_of_cereal * cereal_price) + (num_gallons_of_milk * milk_price)

    # Calculate the number of $10 bills Mark needs to pay
    num_ten_bills = total_cost // 10
    if total_cost % 10 != 0:
        num_ten_bills += 1

    result = num_ten_bills
    return result

print(solution())