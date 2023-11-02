def solution():
    num_hometown = 5
    num_school = 2 * num_hometown
    num_sports = num_hometown + num_school
    total_invites = num_hometown + num_school + num_sports
    remaining_invites = 0.2 * total_invites
    total_guests = total_invites + remaining_invites
    result = total_guests
    return result

print(solution())