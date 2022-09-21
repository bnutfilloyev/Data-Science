import gym
env = gym.make("LunarLander-v2", render_mode="human")
env.action_space.seed(42)

observation, info = env.reset(seed=42, return_info=True)

for _ in range(1000):
    observation, reward, done, info = env.step(env.action_space.sample())

    if done:
        observation, info = env.reset(return_info=True)

env.close()