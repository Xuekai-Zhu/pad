def solution():
    total_requests = 30  # Ziggy gets 30 song requests every night
    electropop = total_requests / 2  # Half the requests are electropop
    dance = electropop / 3  # A third of the electropop requests are dance music
    rock = 5  # Five song requests are rock music
    oldies = rock - 3  # Oldies requests are three less than rock requests
    dj_choice = oldies / 2  # DJ's choice is played half the number of times as oldies
    rap = total_requests - (electropop + dance + rock + oldies + dj_choice)  # Calculate the number of rap requests

    result = rap
    return result

print(solution())