def solution():
    """Ziggy is a club DJ. Typically, Ziggy gets 30 song requests every night. Half the songs requested are electropop. A third of that amount are requests for dance music. Five song requests are rock music, and song requests for oldies are three less in number than rock requests. Ziggy plays a DJ’s choice song half the number of times he plays an oldie. Ziggy also sometimes gets rap song requests. Typically, how many rap songs does Ziggy get requested every night?"""
    # Define the number of song requests Ziggy gets every night
    total_requests = 30

    # Calculate the number of electropop requests
    electropop_requests = total_requests / 2

    # Calculate the number of dance music requests
    dance_requests = electropop_requests / 3

    # Calculate the number of rock music requests
    rock_requests = 5

    # Calculate the number of oldies requests
    oldies_requests = rock_requests - 3

    # Calculate the number of DJ's choice songs played
    dj_choice_songs = oldies_requests / 2

    # Calculate the number of rap song requests
    rap_requests = total_requests - electropop_requests - dance_requests - rock_requests - oldies_requests - dj_choice_songs

    # Display the number of rap song requests
    result = rap_requests
    return result

print(solution())