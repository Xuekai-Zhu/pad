def solution():
    # Define the Catholic and Christian tradition
    catholic = True
    christian = True
    # Check if wearing a crucifixion icon is socially acceptable in the tradition
    if catholic or christian:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())