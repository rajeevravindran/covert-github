from time import sleep

from github.AuthenticatedUser import AuthenticatedUser
from github.Issue import Issue
from github.IssueComment import IssueComment
from github.Repository import Repository

REACTIONS_LIST = [
    "laugh",
    "rocket",
    "-1",
    "heart",
    "eyes",
    "+1",
    "hooray",
    "confused"
]


def waitForSync(sync_comment: IssueComment, content: str, covert_github_user: AuthenticatedUser):
    print(f"[X] Waiting for {content} flag")
    sleep(5)
    while True:
        covert_sync_reaction = [reaction for reaction in sync_comment.get_reactions() if
                                reaction.user == covert_github_user and reaction.content == content]
        if len(covert_sync_reaction) == 1:
            break



def translateMessageToBinary(reactions: list):
    """

    :param reactions: ["laugh", "hooray", "confused"]
    :return: binary_message : "10000011"
    """
    message = ""
    for reaction in REACTIONS_LIST:
        if reaction in reactions:
            message = message + "1"
        else:
            message = message + "0"
    return message


def translateBinaryToGithubReactions(message: str):
    parsed_reactions = []
    for reaction, message_bit in zip(REACTIONS_LIST, message):
        if message_bit == "1":
            parsed_reactions.append(reaction)
    return parsed_reactions


def getBufferWideIssue(repo: Repository, buffer_length: int):
    for issue in repo.get_issues():
        if int(issue.comments) > buffer_length:
            return issue


def chunk_list(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
