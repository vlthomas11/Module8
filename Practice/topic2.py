def average_scores(scoreslist):
    len_scoreslist = len(scoreslist)
    total = 0
    for k, v in scoreslist.items():
        total = total + v

    return total/len_scoreslist


def get_test_scores():
    scores_dict = dict()
    num_scores = int(input("please enter the number of test scores"))
    counter = 0
    while counter < num_scores:
        score = int(input("please enter the score "))
        counter += 1
        scores_dict.update({counter:score})
    avg = average_scores(scores_dict)
    print(avg)


if __name__ == '__main__':
    get_test_scores()

