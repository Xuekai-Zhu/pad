def solution():
    total_requests = 30  # total number of song requests every night
    electropop_requests = total_requests / 2  # half of the songs requested are electropop
    dance_requests = electropop_requests / 3  # a third of the electropop requests are for dance music
    rock_requests = 5  # given that 5 song requests are rock music
    oldies_requests = rock_requests - 3  # the oldies requests are three less in number than rock requests
    dj_choice_requests = oldies_requests / 2  # Ziggy plays a DJ's choice song half the number of times he plays an oldies
    rap_requests = total_requests - (electropop_requests + dance_requests + rock_requests + oldies_requests + dj_choice_requests)  # the remaining requests are for rap songs
    result = rap_requests
    return result

print(solution())