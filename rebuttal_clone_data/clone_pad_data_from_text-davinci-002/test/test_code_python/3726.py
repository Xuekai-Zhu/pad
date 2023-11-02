def solution():
    total_donation = 240
    community_pantry_donation = total_donation / 3
    local_crisis_donation = total_donation / 2
    livelihood_donation = (total_donation - community_pantry_donation - local_crisis_donation) / 4
    contingency_donation = total_donation - (community_pantry_donation + local_crisis_donation + livelihood_donation)
    result = contingency_donation
    return result

print(solution())