import math
from collections import deque

sigma_list = []
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
diff_list = set(num_list)

ans_list = []

# 隣接リスト
adjacent_list = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3, 5, 7],
    [3, 4, 8],
    [3, 7],
    [4, 6, 8],
    [5, 7]
]


class State:
    def __init__(self, board, space, prev):
        self.board = board
        self.space = space
        self.prev = prev


def bfs(start, goal_list):
    q = deque()
    q.append(State(start, start.index(9), None))
    visited = set()
    visited.add(tuple(start))
    count = 1
    while q:
        top_state = q.popleft()
        if top_state.board == goal_list:
            return
        for adj_index in adjacent_list[top_state.space]:
            board = top_state.board[:]
            board[top_state.space] = board[adj_index]
            board[adj_index] = 9
            key = tuple(board)

            if key in visited:
                continue

            if count == 1:
                ans_list.append(State(board, adj_index, top_state).board)

            q.append(State(board, adj_index, top_state))
            visited.add(key)
        count += 1


def print_answer(x):
    if x is not None:
        print_answer(x.prev)
        print(x.board)


if __name__ == '__main__':
    for i in reversed(range(1, 10)):
        NUM = 239145
        sigma_index = ((NUM % math.factorial(i)) // math.factorial(i - 1)) + 1
        sigma_list.append(list(diff_list)[sigma_index - 1])
        diff_list = set(sigma_list) ^ set(num_list)
    bfs(sigma_list, num_list)
    print(ans_list)