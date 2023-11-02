def solution():
    popular_websites_ranking = ["Google", "YouTube", "Facebook", "Amazon", "Twitter", "Instagram", "LinkedIn", "Pinterest", "Snapchat", "Tumblr", "Reddit", "WhatsApp", "TikTok", "Netflix", "PayPal", "Zoom", "Microsoft", "Ebay", "Wikipedia", "Apple"]
    reddit_ranking = popular_websites_ranking.index("Reddit") + 1
    if reddit_ranking <= 18:
        result = "maybe, there might still be internet trolls on Reddit"
    else:
        result = "no, there will probably be internet trolls on Reddit"
    return result

print(solution())