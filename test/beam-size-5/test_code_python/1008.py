def solution():
    
    # Define the initial charge
    charged_charge = 0

    # Calculate the charge lost each hour
    charged_charge_1 = 0.9 * charged_charge

    # Calculate the charge lost each hour for 3 hours
    charged_charge_2 = 0.7 * charged_charge_1

    # Calculate the total capacity after losing for 3 hours
    charged_charge_3 = charged_charge_1 + charged_charge_2

    # Calculate the charge remaining after losing for 3 hours
    charged_charge_4 = 0.28 * charged_charge_2

    # Calculate the final charge
    final_charge = charged_charge_1 + charged_charge_2 + charged_charge_3

    # Display the final charge
    result = final_charge
    return result

print(solution())