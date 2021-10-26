from github import Github
import os
from core import translateBinaryToGithubReactions, REACTIONS_LIST
from collections import Counter
from datetime import datetime

g = Github(os.environ["GITHUB_SENDER_ACCESS_KEY"])

repo = g.get_user("rajeevravindran").get_repo("CSEC.750.Covert.Communications")
# print(repo.raw_data)
covert_user = g.get_user("covert-user")
# ['{0:08b}'.format(i) for i in range(16)]

start_time = datetime.now()
print(f"[X] Sending 16 bytes at {start_time}")
covert_messages = ['00000000', '00000001', '00000010', '00000011', '00000100', '00000101', '00000110', '00000111',
                   '00001000', '00001001', '00001010', '00001011', '00001100', '00001101', '00001110', '00001111']

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
current_time = datetime.now()
print(f"[X] Sending 16 bytes completed at {current_time}")
time_taken = (current_time - start_time).total_seconds()
print(f"[X] Took {time_taken} secs")