def solution():
    # Calculate the total number of hotdogs needed for dinner
    ella_and_emma = 2*2  # Ella and Emma want 2 hotdogs each
    luke = 2*ella_and_emma  # Luke can eat twice the amount of hotdogs as his sisters
    hunter = 1.5*(ella_and_emma+luke)  # Hunter can eat 1.5 times the total amount of his sisters
    total_hotdogs = ella_and_emma + luke + hunter
    result = total_hotdogs
    return result

print(solution())