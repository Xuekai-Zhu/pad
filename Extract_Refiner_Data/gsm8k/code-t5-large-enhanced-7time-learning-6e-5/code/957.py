def solution():
    
    # Define the number of corn chips each person got
    amora_corn_chips = 70
    lainey_corn_chips = 70

    # Calculate the total number of corn chips
    total_corn_chips = amora_corn_chips + lainey_corn_chips

    # Calculate the number of corn chips each person gets
    person1_corn_chips = total_corn_chips // 2
    person2_corn_chips = total_corn_chips - person1_corn_chips - 15
    person3_corn_chips = person1_corn_chips + person2_corn_chips

    # Calculate the total number of corn chips
    total_corn_chips_all = person1_corn_chips + person2_corn_chips + person3_corn_chips

    # Display the total number of corn chips
    result = total_corn_chips_all

print(solution())