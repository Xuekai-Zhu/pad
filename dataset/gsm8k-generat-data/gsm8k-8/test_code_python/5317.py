def solution():
    # Define the initial variables
    medical_expenses = 128
    salary = 160

    # Calculate the amount the couple needs to pay for the medical expenses
    couple_share = medical_expenses / 2 

    # Calculate the remaining amount to be deducted from the house help's salary
    remaining_salary = salary - (medical_expenses / 2)

    # Calculate the amount the husband needs to pay to split the expenses equally with his partner
    husband_share = (couple_share + remaining_salary) / 2 
    result = husband_share
    return result

print(solution())