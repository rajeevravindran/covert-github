from github import Github
import os
from core import translateBinaryToGithubReactions, REACTIONS_LIST
from collections import Counter

g = Github(os.environ["GITHUB_SENDER_ACCESS_KEY"])

repo = g.get_user("rajeevravindran").get_repo("CSEC.750.Covert.Communications")
# print(repo.raw_data)
covert_user = g.get_user("covert-user")

covert_messages = ["01110110"]

for issue in repo.get_issues():
    if int(issue.comments) > 0:
        comments_list = issue.get_comments()
        for covert_message, comment in zip(covert_messages, comments_list):
            all_reactions = comment.get_reactions()
            [reaction.delete() for reaction in all_reactions if reaction.user == covert_user]
            covert_reactions = translateBinaryToGithubReactions(covert_message)
            # clear_covert_reactions = list((Counter(REACTIONS_LIST)-Counter(covert_reactions)).elements())
            for covert_reaction in covert_reactions:
                comment.create_reaction(covert_reaction)
            # for clear_cover_reaction in clear_covert_reactions:
            #     comment.delete_reaction()
