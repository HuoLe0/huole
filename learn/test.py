import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.zeros(4)
step = 0.01
action = [-step, step]
epsilon = 0.9
max_episodes = 100
M_state = 100
N_action = 2
#建立Q表
def build_Qtable(M_state,N_action):
    data = np.zeros((M_state, N_action))
    Q = pd.DataFrame(data,columns=action)
    print(Q)


#生成功率分配因子
def get_a(a):
    for i in range(len(a)):
        a[i] = '%.2f' % np.random.uniform(0,1)
        if np.sum(a) > 1:
            a[i] = 0
    print(a, np.sum(a))


#更新动作
def update_action(a,action):
    for i in range(len(a)):
        if a[i] >= step:
            a[i] = '%.2f' % (a[i] + np.random.choice(action))
        if np.sum(a) > 1:
            a[i] = '%.2f' % (a[i] - step)

    print(a, np.sum(a))

#从Q表选择动作
def choose_action(state, Q):
    state_action = Q.iloc[state, :]
    if np.random.uniform(0,1) > 0.9:
        action_name = np.random.choice(action)

    else:
        action_name = state_action.idxmax()
    return action_name





def RL():
    Q = build_Qtable(M_state, N_action)
    for episode in range(max_episodes):
        step_counter = 0
        s = 0
        is_terminated = False


#更新Q表

build_Qtable(M_state,N_action)
get_a(a)
update_action(a,action)

