def solution():
    """David has a store where he sells cell phones. When he takes inventory at the end of the day, he notices that he has 10 Samsung cell phones but he started the day with 14 Samsung cell phones. Then he notices that he has 5 iPhones and in the initial inventory, but started with 8. His staff then told him that in the afternoon they realized that 2 Samsung cell phones were damaged and 1 iPhone had a manufacturing defect in the screen, so they threw these out during the day. What was the total number of cell phones that were sold today?"""
    # Define the initial inventory of Samsung and iPhones
    start_samsung = 14
    start_iphones = 8

    # Define the inventory at the end of the day
    end_samsung = 10
    end_iphones = 5

    # Define the number of damaged Samsung and iPhones thrown out during the day
    damaged_samsung = 2
    defective_iphones = 1

    # Calculate the total number of Samsung and iPhones sold during the day
    sold_samsung = start_samsung - end_samsung + damaged_samsung
    sold_iphones = start_iphones - end_iphones + defective_iphones

    # Calculate the total number of cell phones sold during the day
    total_sold = sold_samsung + sold_iphones

    # Display the total number of cell phones sold
    result = total_sold
    return result

print(solution())