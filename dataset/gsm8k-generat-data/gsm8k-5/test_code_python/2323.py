def solution():
    invitations_sent = 200  # Jack sent out 200 invitations
    rsvp_percentage = 0.9  # 90% of people RSVPed
    attendance_percentage = 0.8  # 80% of people who RSVPed actually showed up
    no_gifts = 10  # 10 people who showed up didn't get a gift
    gifts_received = invitations_sent * rsvp_percentage * attendance_percentage - no_gifts  # Calculate the number of gifts received
    thank_you_cards_needed = gifts_received  # Jack needs to send thank you cards to everyone who got him a gift
    result = thank_you_cards_needed
    return result

print(solution())