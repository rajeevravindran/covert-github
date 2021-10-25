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


def translateMessageToBinary(reactions: list):
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
