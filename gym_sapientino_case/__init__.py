from gym.envs.registration import register

register(
     id='SapientinoCase-v0',
     entry_point='gym_sapientino_case.env:SapientinoCase',
     max_episode_steps=1000,
)
