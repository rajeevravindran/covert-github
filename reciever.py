from github import Github
import os

# First create a Github instance:

# using an access token
from core import translateMessageToBinary

g = Github(os.environ["GITHUB_RECEIVER_ACCESS_KEY"])

# Then play with your Github objects:
repo = g.get_user("rajeevravindran").get_repo("CSEC.750.Covert.Communications")
# print(repo.raw_data)
covert_user = g.get_user("covert-user")

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
            if covert_message == "00000000":
                break
            print(covert_message)