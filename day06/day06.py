class pathfinding:
    grid = []
    current_pos = (-1, -1)
    dir = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }
    turn_count = 0

    def add_row(self, row):
        for column, item in enumerate(row):
            if item in self.dir:
                self.current_pos = len(self.grid), column

        self.grid.append(row)

    def turn_right(self):
        self.turn_count += 1
        dir_index = list(self.dir.keys()).index(self.grid[self.current_pos[0]][self.current_pos[1]])
        dir_index += 1
        if dir_index > len(self.dir.keys()) - 1:
            dir_index = 0
        self.grid[self.current_pos[0]][self.current_pos[1]] = list(self.dir.keys())[dir_index]

    def walk_path(self):
        current_dir = self.grid[self.current_pos[0]][self.current_pos[1]]
        next_pos = self.current_pos[0] + self.dir[current_dir][0], self.current_pos[1] + self.dir[current_dir][1]

        while -1 < next_pos[0] < len(self.grid) and -1 < next_pos[1] < len(self.grid[0]):

            if self.grid[next_pos[0]][next_pos[1]] == '#':
                self.turn_right()
                current_dir = self.grid[self.current_pos[0]][self.current_pos[1]]
                next_pos = self.current_pos[0] + self.dir[current_dir][0], self.current_pos[1] + self.dir[current_dir][
                    1]
                continue
            self.grid[self.current_pos[0]][self.current_pos[1]] = 'X'
            self.current_pos = next_pos
            self.grid[self.current_pos[0]][self.current_pos[1]] = current_dir

            current_dir = self.grid[self.current_pos[0]][self.current_pos[1]]
            next_pos = self.current_pos[0] + self.dir[current_dir][0], self.current_pos[1] + self.dir[current_dir][1]

        self.grid[self.current_pos[0]][self.current_pos[1]] = 'X'

    def count_visited_locations(self):
        visited_count = 0
        for row in self.grid:
            for location in row:
                if location == 'X':
                    visited_count += 1
        return visited_count


def guard_path(ls):
    path = pathfinding()
    for line in ls:
        path.add_row(list(line.strip()))
    path.walk_path()
    return path.count_visited_locations()
