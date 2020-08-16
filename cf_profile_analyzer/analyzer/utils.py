import requests


def choose_color(rating):
    if rating < 1200:
        color = "#808080"
    elif 1200 <= rating <= 1400:
        color = "#008000"
    elif 1400 <= rating <= 1600:
        color = "#03a89e"
    elif 1600 <= rating <= 1900:
        color = "#0000ff"
    elif 1900 <= rating <= 2100:
        color = "#aa00aa"
    elif 2100 <= rating <= 2300:
        color = "#ff8c00"
    elif 2300 <= rating <= 2400:
        color = "#ff8c00"
    elif 2400 <= rating <= 2600:
        color = "#ff0000"
    elif 2600 <= rating <= 3000:
        color = "#ff0000"
    else:
        color = "#ff0000"

    return color


def get_user_info(handle):
    link = f"https://codeforces.com/api/user.info?handles={handle}"

    data = ''
    try:
        user_info = requests.get(link).json()['result'][0]

        data = {'curRating': user_info['rating'], 'curRank': user_info['rank'], 'maxRating': user_info['maxRating'],
                'friendCount': user_info['friendOfCount'], 'photo': user_info['titlePhoto'],
                'handle': user_info['handle'], 'curColor': choose_color(user_info['rating']),
                'maxColor': choose_color(user_info['maxRating'])}
    except KeyError:
        pass

    return data


def get_contest_info(handle):
    link = f"https://codeforces.com/api/user.rating?handle={handle}"

    data = ''
    try:
        contests = requests.get(link).json()['result']

        ratings = []
        standings = []
        for contest in contests:
            ratings.append(contest['newRating'])
            standings.append(contest['rank'])

        data = {'ratings': ratings, 'minRating': min(ratings), 'minStanding': min(standings),
                'maxStanding': max(standings), 'minColor': choose_color(min(ratings))}
    except KeyError:
        pass

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

    data = ""
    try:
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

        successRatio = round((successfulSubmission/len(submissions))*100,2)
        failedRatio = round((failedSubmission / len(submissions)) * 100,2)
        data = {'totalSub': len(submissions), 'successSub': successfulSubmission, 'failedSub': failedSubmission,
                'topTags': topTags, 'topSuccessIndex': topSuccessIndex, 'topFailedIndex': topFailedIndex,
                'successRatio': successRatio, 'failedRatio': failedRatio}
    except KeyError:
        pass

    return data
