def solution():
    """Mark has a really bad headache.  He takes 2 Tylenol tablets of 500 mg each and he does every 4 hours for 12 hours.  How many grams of Tylenol does he end up taking?"""
    # Calculate the total number of tablets Mark takes
    total_tablets = 2 * (12/4)

    # Calculate the total amount of Tylenol Mark takes in milligrams
    total_tylenol_mg = total_tablets * 500

    # Convert the total amount of Tylenol to grams
    total_tylenol_g = total_tylenol_mg / 1000

    # Display the total amount of Tylenol Mark takes in grams
    result = total_tylenol_g
    return result

print(solution())