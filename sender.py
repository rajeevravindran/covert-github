import random

from github import Github
from github.IssueComment import IssueComment

import os
from core import translateBinaryToGithubReactions, REACTIONS_LIST
from collections import Counter
from itertools import cycle
from datetime import datetime

g = Github(os.environ["GITHUB_SENDER_ACCESS_KEY"])

repo = g.get_user("rajeevravindran").get_repo("CSEC.750.Covert.Communications")
# print(repo.raw_data)
covert_user = g.get_user("covert-user")
# ['{0:08b}'.format(i) for i in range(16)]

start_time = datetime.now()
print(f"[X] Sending 64 bytes at {start_time}")
covert_messages = ['{0:08b}'.format(random.randrange(0, i+1)) for i in range(64)]
print(covert_messages)

def waitForSync(sync_comment: IssueComment, content: str):
    while True:
        covert_sync_reaction = [reaction for reaction in sync_comment.get_reactions() if
                                reaction.user == covert_user and reaction.content == content]
        if len(covert_sync_reaction) == 1:
            break


for issue in repo.get_issues():
    if int(issue.comments) > 0:
        comments_list = issue.get_comments()
        bit_count = 0
        for covert_message, comment in zip(covert_messages, cycle(comments_list)):
            current_time = datetime.now()
            print(f"Sending #{bit_count} {covert_message} on {comment.body}", end="")
            all_reactions = comment.get_reactions()
            [reaction.delete() for reaction in all_reactions if reaction.user == covert_user]
            covert_reactions = translateBinaryToGithubReactions(covert_message)
            # clear_covert_reactions = list((Counter(REACTIONS_LIST)-Counter(covert_reactions)).elements())
            for covert_reaction in covert_reactions:
                comment.create_reaction(covert_reaction)
            print(f", took {(datetime.now() - current_time).total_seconds()} secs")
            # for clear_cover_reaction in clear_covert_reactions:
            #     comment.delete_reaction()
            bit_count = bit_count + 1
current_time = datetime.now()
print(f"[X] Sending 16 bytes completed at {current_time}")
time_taken = (current_time - start_time).total_seconds()
print(f"[X] Took {time_taken} secs")
