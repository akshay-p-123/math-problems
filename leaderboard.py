#appends a line to leaderboard.txt
def write_leaderboard(text):
    with open('leaderboard.txt', 'a') as f:
        f.write(text + '\n')

#shows top 5 on leaderboard
def print_leaderboard(user):
    
    pairs = [] #pairs a username to an individual score; a username can appear more than once

    #read text file
    with open('leaderboard.txt', 'r') as f:
        raw = f.readlines()

    #appends the username-score pairs to pairs
    for i in raw:
        username = i.partition(" ")[0]
        score = i.partition(" ")[2]
        score = int(score.rstrip(i[-1]))
        pairs.append((username, score))


    #arrange in decreasing order
    def key(e):
        return e[1]
    pairs.sort(reverse = True, key=key)


    #return top 5
    text = ""
    try:
        top = []
        for i in range(5):
            top.append(pairs[i])
            text += f"{i + 1}). {pairs[i][0]}     {pairs[i][1]}\n"
    except IndexError:
        text += "No more scores available"    


    #if current user isn't on leaderboard, show them too and what place their high score is
    temp = False
    for i in top:
        if user == i[0]:
            temp = True
            break

    if not temp:
        for i in range(len(pairs) - 1):
            if pairs[i][0] == user:
                text = text + f"\n {i + 1}). {pairs[i][0]}     {pairs[i][1]}"
                break

    return text

