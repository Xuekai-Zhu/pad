def solution():
    total_earnings = 380  # Maya's organization made $380 in total
    broccoli_earnings = 57  # They made $57 from broccoli sales
    
    # Calculate the earnings from carrot sales
    carrot_earnings = 2 * broccoli_earnings

    # Calculate half of the carrot sales and add $16 to get the earnings from spinach sales
    spinach_earnings = (carrot_earnings / 2) + 16

    # Calculate the earnings from cauliflower sales by subtracting the earnings from the other three vegetables from the total earnings
    cauliflower_earnings = total_earnings - broccoli_earnings - carrot_earnings - spinach_earnings
    
    result = cauliflower_earnings
    return result

print(solution())