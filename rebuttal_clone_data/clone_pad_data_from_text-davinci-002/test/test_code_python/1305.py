def solution():
    total_invited = 200
    percent_rsvp = 90
    percent_attend = 80
    people_attending = total_invited * (percent_rsvp / 100) * (percent_attend / 100)
    people_not_attending = total_invited - people_attending
    people_without_gifts = 10
    thank_you_cards_needed = people_attending - people_without_gifts
    result = thank_you_cards_needed
    return result

print(solution())