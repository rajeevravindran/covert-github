from github import Github
import os
from datetime import datetime
from core import translateMessageToBinary, waitForSync

g = Github(os.environ["GITHUB_RECEIVER_ACCESS_KEY"])
repo = g.get_user("rajeevravindran").get_repo("CSEC.750.Covert.Communications")

covert_user = g.get_user("covert-user")

# for issue in repo.get_issues():
#     if int(issue.comments) > 0:
#         comments_list = issue.get_comments()
#         for comment in comments_list:
#             all_reactions = comment.get_reactions()
#             [reaction.delete() for reaction in all_reactions if reaction.user == covert_user]

print(f"Current Rate Limit is {g.get_rate_limit()}")