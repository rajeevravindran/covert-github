from time import sleep

from github import Github
import os
from datetime import datetime
from core import translateMessageToBinary, waitForSync, getBufferWideIssue

g = Github(os.environ["GITHUB_RECEIVER_ACCESS_KEY"])
repo = g.get_user("rajeevravindran").get_repo("CSEC.750.Covert.Communications")
covert_user = g.get_user("covert-user")

BUFFER_SIZE = 16
buffer = ""
issue = getBufferWideIssue(repo, BUFFER_SIZE)

comments_list = issue.get_comments()
firstComment = comments_list[0]

while True:
    start_time = datetime.now()
    print(f"[X] Reading bytes at {start_time}")
    bufferReaction = [reaction for reaction in firstComment.get_reactions() if
                      reaction.user == covert_user and reaction.content == "laugh"]
    if len(bufferReaction) > 0:
        print({
            "message": buffer
        })
        buffer = ""
        bufferReaction[0].delete()
        sleep(2)
        pass
    isFirstFlag = True
    for comment in comments_list:
        if isFirstFlag:
            comment.create_reaction("+1")
            waitForSync(comment, "-1", covert_user)
            firstComment = comment
            isFirstFlag = False
            pass
        reactions = comment.get_reactions()
        covert_reactions = []
        for reaction in reactions:
            if reaction.user == covert_user:
                covert_reactions.append(reaction.content)
        covert_message = int(translateMessageToBinary(covert_reactions),2)
        # if covert_message == "00000000":
        #     break
        if covert_message > 0:
            buffer = buffer + chr(covert_message)
    firstComment.create_reaction("+1")
    current_time = datetime.now()
    print(f"[X] Reading bytes completed at {current_time}")
    time_taken = (current_time - start_time).total_seconds()
    print(f"[X] Took {time_taken} secs")
