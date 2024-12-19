def check_laws(index, page, update, letter_laws):
    page = int(page)
    before = update[:index]
    after = update[index + 1:]
    for before_page in before:
        if int(before_page) in letter_laws[page][1]:
            return False
    for after_page in after:
        if int(after_page) in letter_laws[page][0]:
            return False
    return True


def update_ordering(ls):
    update_start_index = -1
    letter_laws = {}

    for index, line in enumerate(ls):
        if line == '\n':
            update_start_index = index
            break
        else:
            line = line.strip()
            new_law = line.split('|')

            if int(new_law[0]) not in letter_laws:
                letter_laws[int(new_law[0])] = [[], []]
            if int(new_law[1]) not in letter_laws:
                letter_laws[int(new_law[1])] = [[], []]

            letter_laws[int(new_law[0])][1].append(int(new_law[1]))
            letter_laws[int(new_law[1])][0].append(int(new_law[0]))

    mid_sum = 0

    for i in range(update_start_index + 1, len(ls)):
        ls[i] = ls[i].strip()
        update = ls[i].split(',')
        for index, page in enumerate(update):
            correct = check_laws(index, page, update, letter_laws)
            if not correct:
                break
            else:
                if index == len(update) - 1:
                    mid_sum += int(update[int((len(update) - 1) / 2)])
    return mid_sum


def fix_update(update, letter_laws):
    fix_index = 0
    while fix_index != -1:
        fix_index = -1
        for index, page in enumerate(update):
            before = update[:index]
            if page in letter_laws:
                for before_page in before:
                    if before_page in letter_laws[page]:
                        fix_index = index
            if fix_index != -1:
                break

        if fix_index != -1:
            popped_page = update.pop(fix_index)

            new_index = -1
            for index, page in enumerate(update):
                if page in letter_laws[popped_page]:
                    new_index = index
                    break

            update.insert(new_index, popped_page)

    return update


def update_fixing(ls):
    update_start_index = -1
    letter_laws = {}

    for index, line in enumerate(ls):
        if line == '\n':
            update_start_index = index
            break
        else:
            line = line.strip()
            new_law = line.split('|')
            new_law = [int(x) for x in new_law]

            if new_law[0] not in letter_laws:
                letter_laws[new_law[0]] = []

            letter_laws[new_law[0]].append(new_law[1])

    mid_sum = 0

    for i in range(update_start_index + 1, len(ls)):
        ls[i] = ls[i].strip()
        update = ls[i].split(',')
        update = [int(x) for x in update]
        fix = fix_update(update[:], letter_laws)
        if fix != update:
            mid_sum += fix[int((len(fix) - 1) / 2)]

    return mid_sum
