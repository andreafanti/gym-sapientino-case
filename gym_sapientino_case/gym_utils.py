"""Gym utilities."""

from gym import Wrapper
from gym.spaces import Tuple as GymTuple


class SingleAgentWrapper(Wrapper):
    """
    Wrapper for multi-agent OpenAI Gym environment to make it single-agent.

    It adapts a multi-agent OpenAI Gym environment with just one agent
    to be used as a single agent environment.
    In particular, this means that if the observation space and the
    action space are tuples of one space, the new
    spaces will remove the tuples and return the unique space.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the wrapper."""
        super().__init__(*args, **kwargs)

        self.observation_space = self._transform_tuple_space(self.observation_space)
        self.action_space = self._transform_tuple_space(self.action_space)

    def _transform_tuple_space(self, space: GymTuple):
        """Transform a Tuple space with one element into that element."""
        assert isinstance(
            space, GymTuple
        ), "The space is not an instance of gym.spaces.tuples.Tuple."
        assert len(space.spaces) == 1, "The tuple space has more than one subspaces."
        return space.spaces[0]

    def step(self, action):
        """Do a step."""
        state, reward, done, info = super().step([action])
        new_state = state[0]
        return new_state, reward, done, info

    def reset(self, **kwargs):
        """Do a step."""
        state = super().reset(**kwargs)
        new_state = state[0]
        return new_state
