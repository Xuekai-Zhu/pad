def solution():
    croissants_per_dozen = 12  # Dennis needs 6 dozen croissants
    butter_per_dozen = 1  # Dennis uses 1 pound of butter for every dozen croissants he makes
    total_croissants = 6  # Dennis needs to make 6 dozen croissants

    # Calculate the total amount of butter needed
    total_butter = croissants_per_dozen * butter_per_dozen

    # Calculate the amount of butter the promotion will get
    discounted_butter = total_butter / 2

    # Calculate the total cost of 6 pounds of butter
    total_cost = discounted_butter * 4.00
    result = total_cost
    return result

print(solution())