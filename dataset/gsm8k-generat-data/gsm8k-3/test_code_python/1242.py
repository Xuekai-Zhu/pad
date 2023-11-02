def solution():
    """Vinny weighed 300 pounds then lost 20 pounds in the first month of his diet. He continued his diet but each month, he lost half as much weight as he had lost in the previous month. At the start of the fifth month of his diet, he worked harder to lose extra weight then decided to end his diet. If Vinny weighed 250.5 pounds at the end of his diet, how many pounds did he lose throughout the fifth month?"""
    # Define Vinny's starting weight and weight loss values
    vinny_weight = 300
    starting_loss = 20

    # Calculate Vinny's weight loss for each month
    loss_values = [starting_loss, starting_loss/2, starting_loss/4, starting_loss/8, starting_loss/16]

    # Calculate Vinny's weight for each month
    weight_values = [vinny_weight - loss_values[0],
                     weight_values[0] - loss_values[1],
                     weight_values[1] - loss_values[2],
                     weight_values[2] - loss_values[3],
                     weight_values[3] - loss_values[4]]

    # Calculate Vinny's weight loss for the fifth month
    fifth_month_loss = weight_values[4] - 250.5

    # Display Vinny's weight loss for the fifth month
    result = fifth_month_loss
    return result

print(solution())