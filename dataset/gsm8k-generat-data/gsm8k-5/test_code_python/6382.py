def solution():
    bottles_per_case = 24  # Each case contains 24 bottles
    total_cases = 13  # The camp purchased 13 cases of water
    total_groups = 4  # There are 4 groups in the camp

    # Calculate the total number of children in the camp
    total_children = 14 + 16 + 12 + (14 + 16 + 12) / 2  # The fourth group has half the number of the first three groups combined

    # Calculate the total number of bottles needed for the three-day camp
    total_bottles = total_children * 3 * 3  # Each child consumes 3 bottles per day, and the camp is for 3 days

    # Calculate the total number of bottles in the purchased cases
    total_bottles_purchased = bottles_per_case * total_cases

    # Calculate the additional number of bottles needed
    additional_bottles_needed = total_bottles - total_bottles_purchased
    result = additional_bottles_needed
    return result

print(solution())