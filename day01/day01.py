def get_lists(ls):
    left_list = []
    right_list = []
    for line in ls:
        temp = line.split()
        left_list.append(int(temp[0]))
        right_list.append(int(temp[1]))

    return left_list, right_list


def list_distance(ls):
    lists = get_lists(ls)

    left_list = sorted(lists[0])
    right_list = sorted(lists[1])
    dist = 0
    for i in range(0, len(left_list)):
        dist += abs(right_list[i] - left_list[i])
    return dist


def similarity_score(ls):
    lists = get_lists(ls)

    left_list = lists[0]
    right_list = lists[1]
    sim_score = 0
    for num in left_list:
        sim_score += num*right_list.count(num)
    return sim_score
