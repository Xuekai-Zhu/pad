def solution():
    total_earnings = 380
    broccoli_sales = 57
    carrot_sales = broccoli_sales * 2
    spinach_sales = (carrot_sales/2) + 16

    # Calculate the combined sales of broccoli, carrots, and spinach
    combined_sales = broccoli_sales + carrot_sales + spinach_sales

    # Subtract the combined sales from the total earnings to get the sales of cauliflower
    cauliflower_sales = total_earnings - combined_sales
    result = cauliflower_sales
    return result

print(solution())