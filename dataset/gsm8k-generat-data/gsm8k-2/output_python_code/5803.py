def solution():
    """Ziggy gets 30 song requests every night. Half the songs requested are electropop. A third of that amount are requests for dance music. Five song requests are rock music, and song requests for oldies are three less in number than rock requests. Ziggy plays a DJ’s choice song half the number of times he plays an oldie. Ziggy also sometimes gets rap song requests. Typically, how many rap songs does Ziggy get requested every night?"""
    total_requests = 30
    electropop_requests = total_requests / 2
    dance_requests = electropop_requests / 3
    rock_requests = 5
    oldies_requests = rock_requests - 3
    dj_choice_requests = oldies_requests / 2
    rap_requests = total_requests - (electropop_requests + dance_requests + rock_requests + oldies_requests + dj_choice_requests)
    result = rap_requests
    return result

print(solution())