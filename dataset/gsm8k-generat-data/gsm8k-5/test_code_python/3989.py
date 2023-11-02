def solution():
    percent_received_card = 0.3  # Ms. Jones received thank you cards from 30% of her class
    percent_contained_gift_card = 1 / 3  # 1/3 of the thank you cards contained a gift card
    total_gift_card_amount = 50  # Ms. Jones received $50 in gift cards

    # Calculate the total number of students in Ms. Jones' class
    total_class_size = total_gift_card_amount / (percent_received_card * percent_contained_gift_card * 10)

    result = total_class_size
    return result

print(solution())