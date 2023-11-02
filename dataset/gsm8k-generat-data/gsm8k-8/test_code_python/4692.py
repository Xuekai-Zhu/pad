def solution():
    # Define the number of bags raked on Monday and Tuesday
    monday_bags = 5
    tuesday_bags = 3

    # Calculate the total earnings from Monday and Tuesday
    total_earnings = (monday_bags + tuesday_bags) * 4

    # Calculate the earnings from Wednesday
    wednesday_earnings = 68 - total_earnings

    # Calculate the number of bags raked on Wednesday
    wednesday_bags = wednesday_earnings / 4
    result = wednesday_bags
    return result

print(solution())