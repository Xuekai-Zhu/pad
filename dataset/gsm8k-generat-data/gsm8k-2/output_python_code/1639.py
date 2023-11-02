def solution():
    """For Halloween, Taquon, Mack and Jafari put their candy together and they had 418 pieces of candy. If Taquon and Mack each had 171 pieces of candy, how many pieces of candy did Jafari start with?"""
    total_candy = 418
    taquon_candy = 171
    mack_candy = 171
    jafari_candy = total_candy - taquon_candy - mack_candy
    result = jafari_candy
    return result

print(solution())