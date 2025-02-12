import praw
reddit = praw.Reddit( client_id = '1Q4FiwYUJqCuPV1D4ipCLQ',
                      client_secret = '6UbMVhlWSuLgL3meerKJbpSZfrnt4w',
                      user_agent = 'Post automatically',
                      username='satanevil_69',
                      password='v7m_gBy!k-cP6#V'
)

subreddit_name = "developersIndia"  # Change to your desired subreddit
# Title and content of the post
title = "My first automated post using Python! Please upvote this"
selftext = "Hello Reddit! This post was made using a Python script."



# Submit the post

subreddit = reddit.subreddit(subreddit_name)
choices = list(subreddit.flair.link_templates.user_selectable())
template_id = next(x for x in choices if x["flair_text"] == "Suggestions")["flair_template_id"]
subreddit.submit(title=title, selftext=selftext,flair_id=template_id)
print(f"Posted to Reddit: {title}")