def solution():
    
    # Define the total amount divided by the three people
    total_amount = 1920

    # Calculate the amount taken by the second person
    second_person = total_amount + 80

    # Calculate the amount taken by the third person
    third_person = second_person * 2

    # Calculate the total amount taken by all three people
    total_taken = second_person + third_person

    # Calculate the amount taken by the first person
    first_person = total_amount - total_taken

    # Display the amount taken by the first person
    result = first_person
    return result

print(solution())