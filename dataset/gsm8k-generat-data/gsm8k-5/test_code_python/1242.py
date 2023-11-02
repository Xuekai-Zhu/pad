def solution():
    starting_weight = 300  # Vinny weighed 300 pounds at the start of his diet
    first_month_loss = 20  # Vinny lost 20 pounds in the first month
    total_loss = first_month_loss
    
    # Calculate how much Vinny lost in each subsequent month
    for i in range(2, 5):
        loss_this_month = 0.5 * total_loss  # Vinny lost half as much as the previous month
        total_loss += loss_this_month
    
    # Calculate the amount Vinny had to lose in the fifth month
    fifth_month_loss = starting_weight - 250.5 - total_loss
    
    result = fifth_month_loss
    return result

print(solution())