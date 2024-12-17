class wordSearch:
    wordGrid = []

    def add_line(self, line):
        self.wordGrid.append(line)

    def count_xmas(self):
        xmas_count = 0
        for line_num, line in enumerate(self.wordGrid):
            for letter_num, letter in enumerate(line):
                if self.wordGrid[line_num][letter_num] == 'X':
                    xmas_count += self.mas_finder(line_num, letter_num, 0, 1, "MAS")
                    xmas_count += self.mas_finder(line_num, letter_num, 1, 1, "MAS")
                    xmas_count += self.mas_finder(line_num, letter_num, 1, 0, "MAS")
                    xmas_count += self.mas_finder(line_num, letter_num, 1, -1, "MAS")
                    xmas_count += self.mas_finder(line_num, letter_num, 0, -1, "MAS")
                    xmas_count += self.mas_finder(line_num, letter_num, -1, -1, "MAS")
                    xmas_count += self.mas_finder(line_num, letter_num, -1, 0, "MAS")
                    xmas_count += self.mas_finder(line_num, letter_num, -1, 1, "MAS")
        return xmas_count

    def mas_finder(self, line_num, letter_num, line_delta, letter_delta, search_phrase):
        line_num += line_delta
        letter_num += letter_delta
        # stop on edge
        if line_num < 0 or letter_num < 0 or line_num > len(self.wordGrid) - 1 or letter_num > len(
                self.wordGrid[0]) - 1:
            return 0

        # print(line_num, letter_num)
        if self.wordGrid[line_num][letter_num] == search_phrase[0]:
            # stop on last letter
            if len(search_phrase) == 1:
                return 1
            return self.mas_finder(line_num, letter_num, line_delta, letter_delta, search_phrase[1:])
        # stop on wrong letter
        else:
            return 0


class xSearch:
    letterGrid = []

    def add_line(self, line):
        self.letterGrid.append(line)

    def count_x_mas(self):
        x_mas_count = 0
        for line_num, line in enumerate(self.letterGrid):
            for letter_num, letter in enumerate(line):
                if self.letterGrid[line_num][letter_num] == 'A':
                    x_mas_count += self.mas_checker(line_num, letter_num)
        return x_mas_count

    def mas_checker(self, line_n, letter_n):
        # stop on edge
        if line_n < 1 or letter_n < 1 or line_n > len(self.letterGrid) - 2 or letter_n > len(
                self.letterGrid[0]) - 2:
            return 0
        mas1 = self.letterGrid[line_n-1][letter_n-1] + 'A' + self.letterGrid[line_n+1][letter_n+1]
        mas2 = self.letterGrid[line_n+1][letter_n-1] + 'A' + self.letterGrid[line_n-1][letter_n+1]
        if (mas1 == 'MAS' or mas1 == 'SAM') and (mas2 == 'MAS' or mas2 == 'SAM'):
            return 1
        return 0


def xmas_search(ls):
    search = wordSearch()
    for line in ls:
        search.add_line(list(line.strip()))
    total = search.count_xmas()
    return total


def x_mas_search(ls):
    search = xSearch()
    for line in ls:
        search.add_line(list(line.strip()))
    total = search.count_x_mas()
    return total
