import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    done = False
    t = 0
    while not done:
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        t = t + 1
    print("Episode {} finished after {} timesteps".format(i_episode, t+1))




