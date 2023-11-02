def solution():
    """Vinny weighed 300 pounds then lost 20 pounds in the first month of his diet. He continued his diet but each month, he lost half as much weight as he had lost in the previous month. At the start of the fifth month of his diet, he worked harder to lose extra weight then decided to end his diet. If Vinny weighed 250.5 pounds at the end of his diet, how many pounds did he lose throughout the fifth month?"""
    # Define Vinny's initial weight and weight loss in the first month
    initial_weight = 300
    first_month_loss = 20

    # Define the weight loss for each subsequent month
    monthly_loss = first_month_loss / 2

    # Define Vinny's weight at the start of the fifth month
    weight_fifth_month = 250.5

    # Calculate Vinny's weight at the start of the fourth month
    weight_fourth_month = weight_fifth_month + monthly_loss

    # Calculate Vinny's weight at the start of the third month
    weight_third_month = weight_fourth_month + monthly_loss

    # Calculate Vinny's weight at the start of the second month
    weight_second_month = weight_third_month + monthly_loss

    # Calculate Vinny's weight at the start of the first month
    weight_first_month = weight_second_month + monthly_loss

    # Calculate the total weight loss throughout the fifth month
    weight_loss_fifth_month = weight_fourth_month - weight_fifth_month

    # Return the result
    result = weight_loss_fifth_month
    return result

print(solution())