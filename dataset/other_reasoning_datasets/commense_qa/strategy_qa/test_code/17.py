def solution():
    harry_potter_characters_practice_magic = True
    major_world_religions = ["Christianity", "Islam", "Judaism"]
    persecuted_as_pagans = False
    for religion in major_world_religions:
        if religion == "Islam":
            persecuted_as_pagans = True
    if harry_potter_characters_practice_magic and persecuted_as_pagans:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())