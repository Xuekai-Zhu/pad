def solution():
    thank_you_rate = 0.3
    gift_card_rate = 1/3
    gift_card_value = 10
    total_gift_card_value = 50

    # Calculate the number of students who gave thank you cards
    num_thank_you = thank_you_rate * total_gift_card_value / gift_card_value

    # Calculate the total number of students in Ms. Jones' class
    total_students = num_thank_you / gift_card_rate
    result = total_students
    return result

print(solution())