def solution():
    sloth_algae = True
    sloth_moths_feed_on_algae = True
    sloth_moth_caterpillars_feed_on_dung = True
    sloths_defecate_far_from_abode = True
    if sloth_algae and sloth_moths_feed_on_algae and sloth_moth_caterpillars_feed_on_dung and not sloths_defecate_far_from_abode:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())