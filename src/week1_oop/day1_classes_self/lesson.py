from __future__ import annotations

"""
DAY 1 — Classes, Objects & self
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Wrap data + actions inside one blueprint (Class); create objects from it.

WHY IT MATTERS FOR AI:
  Every Scikit-Learn / PyTorch model is an instance of a class.
  When you write `model = LinearRegression()` or `model = nn.Linear(10, 3)`,
  you're calling a constructor. The `self` inside that class lets it hold
  its own weights, config, and state.

RULE: Write every line yourself. No AI. The tests will tell you if you're right.
"""


# ── Concept ────────────────────────────────────────────────────────
# A class is a blueprint. An object is an instance built from that blueprint.
# `self` is the object itself — it's how a method knows WHICH instance it's
# operating on.
#
#     class Dog:
#         def __init__(self, name: str) -> None:
#             self.name = name          # instance attribute
#
#         def bark(self) -> str:
#             return f"{self.name} says woof!"
#
#     buddy = Dog("Buddy")
#     print(buddy.bark())               # "Buddy says woof!"
#
# See how `self` carries the instance's data? That's the core idea.
# ───────────────────────────────────────────────────────────────────


# ── EXERCISE 1: Your first class ───────────────────────────────────
# TODO: Define a class `ModelConfig` that holds configuration for an ML model.
# Requirements:
#   - __init__ takes: model_name: str, learning_rate: float, max_epochs: int
#   - Stores all three as instance attributes
#   - Has a method `summary()` that returns a formatted string:
#     "ModelConfig(name={model_name}, lr={learning_rate}, epochs={max_epochs})"
#
# Write your code below, replacing the `...` placeholders.
# ───────────────────────────────────────────────────────────────────

class ModelConfig:
    def __init__(self, model_name: str, learning_rate: float, max_epochs: int) -> None:
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs

    def summary(self) -> str:
        return f"ModelConfig(name={self.model_name}, lr={self.learning_rate}, epochs={self.max_epochs})"


# ── EXERCISE 2: Multiple instances ─────────────────────────────────
# TODO: Create TWO instances of ModelConfig and call summary() on each.
# Store the results in a list called `summaries`.
#
# Instance A: model_name="gpt-4o",   learning_rate=1e-5, max_epochs=3
# Instance B: model_name="resnet50", learning_rate=1e-3, max_epochs=50
# ───────────────────────────────────────────────────────────────────

summaries: list[str] = []

# YOUR CODE HERE:
config_a = ModelConfig("gpt-4o", 1e-5, 3)
config_b = ModelConfig("resnet50", 1e-3, 50)

summaries.append(config_a.summary())
summaries.append(config_b.summary())


# ── EXERCISE 3: Instance state is isolated ─────────────────────────
# TODO: Write a function `cross_validate(configs: list[ModelConfig])`
# that takes a list of configs and returns a dict mapping each
# model_name -> {"lr": learning_rate, "epochs": max_epochs}.
#
# This demonstrates that each instance carries its OWN state.
# ───────────────────────────────────────────────────────────────────

def cross_validate(configs: list[ModelConfig]) -> dict[str, dict[str, float | int]]:
    result: dict[str, dict[str, float | int]] = {}
    for config in configs:
        result[config.model_name] = {
            "lr": config.learning_rate,
            "epochs": config.max_epochs,
        }
    return result


# ── EXERCISE 4: Real-world pattern — Model wrapper ────────────────
# TODO: Complete the class `SimpleModel` below.
#
# This mirrors how PyTorch/sklearn work: you create a model object,
# configure it, then "train" it. The instance holds its trained state.
#
# Hint: `self.trained` should start as False and become True after fit().
# ───────────────────────────────────────────────────────────────────

class SimpleModel:
    """A simplified model that remembers its trained state."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.trained = False
        self.training_loss: float | None = None

    def fit(self, data_size: int) -> str:
        # TODO: Set self.trained = True and self.training_loss to
        #       a computed value: 100.0 / data_size
        #       Return: f"{self.name} trained on {data_size} samples"
        self.trained = True
        self.training_loss = 100.0 / data_size
        return f"{self.name} trained on {data_size} samples"
