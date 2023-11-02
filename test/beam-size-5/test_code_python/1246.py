def solution():
    
    # Define the number of bags of chips and the number of chips per bag
    bags_of_chips = 2
    chips_per_bag = 55

    # Calculate the total number of chips
    total_chips = bags_of_chips * chips_per_bag

    # Calculate the number of chips each person gets if they all get the same number
    chips_per_person = total_chips / 5

    # Display the number of chips each person gets
    result = chips_per_person
    return result

print(solution())