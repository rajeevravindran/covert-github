from github import Github
import os
from datetime import datetime
from core import translateMessageToBinary

g = Github(os.environ["GITHUB_RECEIVER_ACCESS_KEY"])
repo = g.get_user("rajeevravindran").get_repo("CSEC.750.Covert.Communications")
covert_user = g.get_user("covert-user")
start_time = datetime.now()
print(f"[X] Reading bytes at {start_time}")

for issue in repo.get_issues():
    if int(issue.comments) > 0:
        comments_list = issue.get_comments()
        for comment in comments_list:
            reactions = comment.get_reactions()
            covert_reactions = []
            for reaction in reactions:
                if reaction.user == covert_user:
                    covert_reactions.append(reaction.content)
            covert_message = translateMessageToBinary(covert_reactions)
            # if covert_message == "00000000":
            #     break
            print(covert_message)
current_time = datetime.now()
print(f"[X] Reading bytes completed at {current_time}")
time_taken = (current_time - start_time).total_seconds()
print(f"[X] Took {time_taken} secs")
