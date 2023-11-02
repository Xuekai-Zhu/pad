def solution():
    """The eighth-grade class held a bake-off. Kelsie made two times more cookies than Josh. Josh made one-fourth the number of cookies that Suzanne made. If Suzanne made 36 cookies, how many did Kelsie make?"""
    suzanne_cookies = 36
    josh_cookies = suzanne_cookies / 4
    kelsie_cookies = josh_cookies * 2
    result = kelsie_cookies
    return result

print(solution())