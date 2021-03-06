from typing import Any


class LinearAnnealer:
    """Linear annealing for training.

    Args:
        init (float): Initial value.
        final (float): Final value.
        steps (int): Number of annealing steps.
    """

    def __init__(
        self, init: float = 0.0, final: float = 1.0, steps: int = 3000, **kwargs: Any
    ) -> None:

        self.init = init
        self.final = final
        self.steps = steps

        self.t = 0
        self.current = init

    def __iter__(self) -> "LinearAnnealer":
        return self

    def __next__(self) -> float:
        self.t += 1
        value = min(
            self.init + (self.final - self.init) * self.t / self.steps,
            self.final,
        )
        self.current = value

        return value
