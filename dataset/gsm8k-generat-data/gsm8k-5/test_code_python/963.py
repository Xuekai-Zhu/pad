def solution():
    total_guests = 80  # Oleg is organizing an event with 80 guests
    num_men = 40  # 40 of them are men
    num_women = num_men / 2  # Half the number of men are women
    num_children = total_guests - num_men - num_women  # The rest are children
    num_children += 10  # If Oleg adds 10 children to the guest list

    result = num_children
    return result

print(solution())