"""Tests for Day 1 — Classes, Objects & self."""

from src.week1_oop.day1_classes_self.lesson import (
    ModelConfig,
    SimpleModel,
    cross_validate,
    summaries,
)


class TestModelConfig:
    """Exercises 1-3: building classes, instances, state isolation."""

    def test_exercise1_attributes(self) -> None:
        cfg = ModelConfig("test", 0.01, 10)
        assert cfg.model_name == "test"
        assert cfg.learning_rate == 0.01
        assert cfg.max_epochs == 10

    def test_exercise1_summary_format(self) -> None:
        cfg = ModelConfig("bert-base", 2e-5, 5)
        expected = "ModelConfig(name=bert-base, lr=2e-05, epochs=5)"
        assert cfg.summary() == expected

    def test_exercise2_two_instances(self) -> None:
        """Verify exactly two summaries were created with correct values."""
        assert len(summaries) == 2
        assert "gpt-4o" in summaries[0]
        assert "resnet50" in summaries[1]

    def test_exercise3_state_isolation(self) -> None:
        cfg1 = ModelConfig("model_a", 0.1, 10)
        cfg2 = ModelConfig("model_b", 0.01, 100)
        result = cross_validate([cfg1, cfg2])
        assert result == {
            "model_a": {"lr": 0.1, "epochs": 10},
            "model_b": {"lr": 0.01, "epochs": 100},
        }
        # Mutating the result should NOT affect originals
        result["model_a"]["lr"] = 999
        assert cfg1.learning_rate == 0.1


class TestSimpleModel:
    """Exercise 4: real-world model wrapper pattern."""

    def test_initial_state(self) -> None:
        m = SimpleModel("classifier")
        assert m.name == "classifier"
        assert m.trained is False
        assert m.training_loss is None

    def test_fit_sets_state(self) -> None:
        m = SimpleModel("regressor")
        msg = m.fit(100)
        assert m.trained is True
        assert m.training_loss == 1.0  # 100.0 / 100
        assert msg == "regressor trained on 100 samples"

    def test_fit_different_sizes(self) -> None:
        m = SimpleModel("multi")
        m.fit(50)
        assert m.training_loss == 2.0  # 100.0 / 50
        m.fit(200)
        assert m.training_loss == 0.5  # 100.0 / 200
