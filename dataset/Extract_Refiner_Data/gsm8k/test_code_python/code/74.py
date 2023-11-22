def solution():
    
    # Define the price of each flower in packages
    package_3_price = 2.5
    package_2_price = 1

    # Define the number of flowers Vincent can buy in packages of 3 and 2
    num_packages_3 = 18
    num_packages_2 = 18

    # Calculate the total cost of buying 18 flowers at the better price
    total_cost_3 = num_packages_3 * package_3_price
    total_cost_2 = num_packages_2 * package_2_price
    total_cost_all = total_cost_3 + total_cost_2

    # Calculate the amount saved by buying 18 flowers at the better price
    amount_saved = total_cost_all - total_cost_all

    # Display the amount saved
    result = amount_saved
    return result

print(solution())