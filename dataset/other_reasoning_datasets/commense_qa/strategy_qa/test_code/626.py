def solution():
    sponsor = "Audible"
    ad_type = "audiobook subscription service"
    ad_discussion = "discussing a book that the speaker has recently listened to"
    unsolicited_advice = False
    if sponsor == "Audible" and ad_type == "audiobook subscription service" and ad_discussion in video_description:
        unsolicited_advice = True
    if unsolicited_advice:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())