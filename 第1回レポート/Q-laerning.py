# 最終的に得られたQ値は以下の通り：
#          a0       a1        a2         a3
#  s00   24.010    34.300    16.807    24.010
#  s01   34.300    49.000    24.010    24.010
#  s02   49.000    70.000    34.300    34.300
#  s03   70.000   100.000    49.000    49.000
#  s04    0.000     0.000     0.000     0.000
#  s10   24.010    24.010    11.765    16.807
#  s11   34.300    24.010    16.807    16.807
#  s12    9.000    49.000    24.010    34.300
#  s13   70.000    70.000    34.300    34.300
#  s14  100.000    70.000    49.000    49.000
#  s20   16.807    16.807     8.235    11.765
#  s21   24.010    16.807    11.765    11.765
#  s22   34.300    34.300    34.300    24.010
#  s23   49.000    49.000    49.000    24.010
#  s24   70.000    49.000    70.000    34.300
#  s30   11.765    11.765    11.765     8.235
#  s31   16.807    11.765    16.807     8.235
#  s32   24.010    49.000    24.010    34.300
#  s33   34.300    70.000    20.000    34.300
#  s34   49.000    70.000   100.000    49.000
#  s40    8.235    16.807    11.765    11.765
#  s41   11.765    24.010    16.807    11.765
#  s42   34.300    20.000    24.010    16.807
#  s43   49.000   100.000    70.000    24.010
#  s44    0.000     0.000     0.000     0.000

import numpy as np
import random

N = 1000000  # 試行回数
n = 5  # 状態数
m = 4  # アクション数: 上, 右, 下, 左の4種類
alpha = 0.1  # 学習率
gamma = 0.7  # 割引率

# 報酬と遷移先の定義
rewards = np.zeros((n, n, m))
rewards[4, 2, 1] = rewards[3, 3, 2] = -50  # Vに着いたら−50の報酬
rewards[0, 3, 1] = rewards[1, 4, 0] = rewards[4, 3, 1] = rewards[3, 4, 2] = 100  # Gに着いたら+100の報酬
# 初期化
Q = np.zeros((n, n, m))

# 各行動に対する遷移先
transitions = np.array([(-1, 0), (0, 1), (1, 0), (0, -1)])

# 壁の定義
walls = [((1, 1), (1, 2)), ((2, 1), (2, 2)), ((3, 1), (3, 2))]


# ランダムにアクションを選択
def choose_action():
    return random.randint(0, m - 1)

# 状態の更新
def update_state(state, action):
    new_state = (state[0] + transitions[action][0], state[1] + transitions[action][1])
    # マップの外に出る場合や壁を通過する場合、状態を更新しない
    if (new_state[0] < 0 or new_state[0] >= n or new_state[1] < 0 or new_state[1] >= n) or ((state, new_state) in walls or (new_state, state) in walls):
        new_state = state
    return new_state

# Q学習の実行
for round in range(N):
    print("Progress : {}%\r".format(100*round/N),end="")
    state = (2, 0)  # 初期状態
    while True:
        action = choose_action()
        next_state = update_state(state, action)
        next_q = np.max(Q[next_state[0], next_state[1]])  # 次の状態での最大Q値
        Q[state[0], state[1], action] = (1 - alpha) * Q[state[0], state[1], action] + alpha * (rewards[state[0], state[1], action] + gamma * next_q)
        state = next_state
        if state in [(0, 4),(4, 4)]:  # Gに着いたら初期状態に戻る
            break
    if round == N - 1:
        for i in range(n):
            for j in range(n):
                print(f"q[{i},{j}, a0]: {Q[i, j, 0]:.06f}")
                print(f"q[{i},{j}, a1]: {Q[i, j, 1]:.06f}")
                print(f"q[{i},{j}, a2]: {Q[i, j, 2]:.06f}")
                print(f"q[{i},{j}, a3]: {Q[i, j, 3]:.06f}")
