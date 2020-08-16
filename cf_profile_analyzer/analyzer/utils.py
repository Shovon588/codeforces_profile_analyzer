import requests


def get_user_info(handle):
    link = f"https://codeforces.com/api/user.info?handles={handle}"

    try:
        user_info = requests.get(link).json()['result'][0]

        data = {'curRating': user_info['rating'], 'curRank': user_info['rank'], 'maxRating': user_info['maxRating'],
            'friendCount': user_info['friendOfCount'], 'photo': user_info['titlePhoto'], 'handle': user_info['handle']}
    except KeyError:
        data = {"error": "User handle not found."}
    return data


def get_contest_info(handle):
    link = f"https://codeforces.com/api/user.rating?handle={handle}"
    contests = requests.get(link).json()['result']

    ratings = []
    standings = []
    for contest in contests:
        ratings.append(contest['newRating'])
        standings.append(contest['rank'])

    data = {'ratings': ratings, 'minRating': min(ratings), 'minStanding': min(standings), 'maxStanding': max(standings)}

    return data


def get_top_five(dictionary):
    tags = []
    for key, value in dictionary.items():
        tags.append((value, key))

    tags.sort(reverse=True)
    tags = tags[:5]
    top_five = {}
    for key, value in tags:
        top_five[value] = key

    return top_five


def get_submission_info(handle):
    link = f"https://codeforces.com/api/user.status?handle={handle}"
    submissions = requests.get(link).json()['result']

    successfulSubmission = 0
    failedSubmission = 0
    favProgTag = {}
    successProblemIndex = {}
    failedProblemIndex = {}

    for submission in submissions:
        if submission['verdict'] == 'OK':
            successfulSubmission += 1
            tags = submission['problem']['tags']
            for tag in tags:
                if tag not in favProgTag:
                    favProgTag[tag] = 1
                else:
                    favProgTag[tag] += 1

            index = submission['problem']['index']
            if index in successProblemIndex:
                successProblemIndex[index] += 1
            else:
                successProblemIndex[index] = 1
        else:
            failedSubmission += 1
            index = submission['problem']['index']
            if index in failedProblemIndex:
                failedProblemIndex[index] += 1
            else:
                failedProblemIndex[index] = 1

    topTags = get_top_five(favProgTag)
    topSuccessIndex = get_top_five(successProblemIndex)
    topFailedIndex = get_top_five(failedProblemIndex)

    data = {'successSub': successfulSubmission, 'failedSub': failedSubmission, 'topTags': topTags,
            'topSuccessIndex': topSuccessIndex, 'topFailedIndex': topFailedIndex}

    return data
