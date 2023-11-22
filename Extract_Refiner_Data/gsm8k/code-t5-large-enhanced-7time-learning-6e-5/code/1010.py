def solution():
    
    # Define the prices of peaches, pears, apples, kiwis, and plums
    peach_price = 0.5
    pear_price = 0.75
    apple_price = 0.75
    kiwis_price = 1
    plum_price = 0.25

    # Define the number of peaches, pears, kiwis, and apples purchased
    peaches_purchased = 3
    pears_purchased = 4
    kiwis_purchased = 2
    apples_purchased = 5

    # Calculate the total cost of the purchase
    total_cost = (peaches_purchased * peach_price) + (peaches_purchased * pear_price) + (apples_purchased * apple_price) + (kiwis_purchased * kiwis_price)

    # Calculate the remaining budget after paying for tax
    remaining_budget = 10 - total_cost

    #

print(solution())