import random

from github import Github

import os
from core import translateBinaryToGithubReactions, waitForSync, getBufferWideIssue
from itertools import cycle
from datetime import datetime

g = Github(os.environ["GITHUB_SENDER_ACCESS_KEY"])

repo = g.get_user("rajeevravindran").get_repo("CSEC.750.Covert.Communications")
# print(repo.raw_data)
covert_user = g.get_user("covert-user")
# ['{0:08b}'.format(i) for i in range(16)]

start_time = datetime.now()
print(f"[X] Sending 64 bytes at {start_time}")
covert_messages = ["00000000"] + ['{0:08b}'.format(random.randrange(0, 64)) for i in range(16)]
print(covert_messages)
BUFFER_SIZE = 16

issue = getBufferWideIssue(repo, BUFFER_SIZE)

firstComment = None

comments_list = issue.get_comments()
bit_count = 0
isFirstFlag = True
for covert_message, comment in zip(covert_messages, cycle(comments_list)):
    if isFirstFlag:
        waitForSync(comment, "+1", covert_user)
        isFirstFlag = False
        firstComment = comment
        pass
    current_time = datetime.now()
    print(f"Sending #{bit_count} {covert_message} on {comment.body}", end="")
    all_reactions = comment.get_reactions()
    [reaction.delete() for reaction in all_reactions if reaction.user == covert_user]
    covert_reactions = translateBinaryToGithubReactions(covert_message)
    # clear_covert_reactions = list((Counter(REACTIONS_LIST)-Counter(covert_reactions)).elements())
    for covert_reaction in covert_reactions:
        comment.create_reaction(covert_reaction)
    print(f", took {(datetime.now() - current_time).total_seconds()} secs.")
    # for clear_cover_reaction in clear_covert_reactions:
    #     comment.delete_reaction()
    bit_count = bit_count + 1
firstComment.create_reaction("-1")

[reaction.delete() for reaction in firstComment.get_reactions() if reaction.user == covert_user]

current_time = datetime.now()
print(f"[X] Sending 16 bytes completed at {current_time}")
time_taken = (current_time - start_time).total_seconds()
print(f"[X] Took {time_taken} secs")
