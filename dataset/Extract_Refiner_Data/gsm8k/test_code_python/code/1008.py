def solution():
    
    # Define the initial charge percentage
    initial_charge_percentage = 0.9

    # Calculate the total capacity of the power bank
    total_capacity = 100

    # Calculate the charge percentage after the power bank loss
    power_bank_loss_percentage = 0.9
    power_bank_loss = power_bank_loss_percentage * total_capacity

    # Calculate the total capacity after the battery loss
    battery_loss_percentage = 0.7
    battery_loss = battery_loss_percentage * total_capacity

    # Calculate the total charge percentage after the battery loss
    total_charge_percentage = power_bank_loss + battery_loss

    # Calculate the charge remaining
    remaining_charge = total_capacity * initial_charge_percentage

    # Calculate the final charge
    final_charge = total_charge_percentage + remaining_charge

    # Display the final charge
    result = final_charge
    return result

print(solution())