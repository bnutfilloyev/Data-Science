import gym
env = gym.make("ALE/Pong-v5", render_mode='human')
observation, info = env.reset(seed=42, return_info=True)
for _ in range(1000):
    # env.render()
#    action = policy(observation)  # User-defined policy function
    action = env.action_space.sample()  # Random action
    observation, reward, done, info = env.step(action)

    if done:
        observation, info = env.reset(return_info=True)
env.close()