def solution():
    """Mark has a really bad headache. He takes 2 Tylenol tablets of 500 mg each and he does every 4 hours for 12 hours. How many grams of Tylenol does he end up taking?"""
    # Define the number of tablets and the dosage of each tablet
    num_tablets = 2
    tablet_dosage = 500 # in mg

    # Calculate the total dosage of Tylenol taken in 12 hours
    total_dosage = num_tablets * tablet_dosage * 3 # 12 hours / 4 hours = 3 doses

    # Convert the dosage from milligrams to grams
    total_dosage_grams = total_dosage / 1000

    result = total_dosage_grams
    return result

print(solution())