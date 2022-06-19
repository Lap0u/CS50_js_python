def createDic(id_list):
    data ={}
    for user in id_list:
        temp = {}
        data[user] = temp
    return data

def addVotes(data, report):
    splited = []
    for line in report:
        splited = line.split()
        data[splited[0]][splited[1]] = True

def getBans(id_list, data, count):
    bans = {}
    for user in id_list:
        bans[user] = 0
    for user in data:
        for votes in data[user]:
            if data[user][votes] == True:
                bans[votes] += 1
    res = {}
    for user in id_list:
        if bans[user] >= count:
            res[user] = True
        else:
            res[user] = False
    return res

def getAnswer(bans, data):
    answer = []
    i = 0
    for user in data:
        answer.append(0)
        for votes in data[user]:
            if (bans[votes] == True and data[user][votes] == True):
                answer[i] += 1
        i += 1
    return answer

def solution(id_list, report, k):
    data = createDic(id_list)
    addVotes(data, report)
    bans = getBans(id_list, data, k)
    answer = getAnswer(bans, data)
    return answer

def test():
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    # id_list = ["muzi", "frodo", "apeach"]
    # report = ["muzi frodo"]

    k = 2
    solution(id_list, report, k)

test()