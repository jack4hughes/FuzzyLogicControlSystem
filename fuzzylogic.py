import numpy as np
import matplotlib.pyplot as plt
from typing import Dict
from funcs import create_clipped_func, fuzzy_and, create_triangle_func, create_normal_func

vect = np.arange(0, 5, 0.001)


class FuzzyLogicController:
    """A class that stores our fuzzy logic asttributes. At the moment this only works with a single input and output system, a system with more than one input may need a more complex class."""
    def __init__(
        self,
        inputs: Dict[str, callable],
        outputs: Dict[str, callable],
        links: Dict[str, str],
        plot_functions: bool = True,
        input_limits=(0, 5),
        output_limits=(-2, 2),
        precision=0.1,
    ):
        self.inputs = inputs
        self.outputs = outputs

        self.input_range = (-2, 2)
        self.output_range = (-2, 2)
        self.links = links
        self.colours = ["red", "blue", "green"]
        self.input_limits = input_limits
        self.output_limits = output_limits
        self.precision = precision

        for name, func in self.inputs.items():
            print(f"created input: {name}, {func}")

        if plot_functions is True:
            self.plot_inputs()

        for name, func in self.outputs.items():
            print(f"created output: {name}, {func}")

        if plot_functions is True:
            self.plot_outputs()
            self.plot_inputs()

    def plot_inputs(self):
        x_range = np.arange(*self.input_limits, self.precision)
        colours = iter(self.colours)
        for key, func in self.inputs.items():
            plt.figure("inputs")
            colour = next(colours)
            plt.plot(x_range, func(x_range), label=key, color=colour)
            plt.legend()
            plt.title("inputs")

    def plot_outputs(self):
        x_range = np.arange(*self.output_limits, self.precision)
        colours = iter(self.colours)

        for name, func in self.outputs.items():
            colour = next(colours)
            plt.figure("outputs")
            plt.plot(x_range, func(x_range), label=name, color=colour)
            plt.legend()
            plt.title("outputs")

    def create_control_function(self, value=1):
        clipped_value = np.clip(value, *self.input_limits)
        combined_logic = []
        for input_logic, output_logic in input_output_links.items():
            input_func = input_fuzzifier[input_logic]
            output_func = output_fuzzifier[output_logic]
            input_max = input_func(clipped_value)

            output_func = create_clipped_func(output_func, input_max)

            combined_logic.append(output_func)

        return fuzzy_and(*combined_logic)

    def calculate_centroid(self, x_range, function):
        # Centroid formula: Σ(x * μ(x)) / Σ(μ(x))
        numerator = np.sum(x_range * function(x_range))
        denominator = np.sum(function(x_range))

        return numerator / denominator

    def calculate_control_output(self, control_input, show_plot=True):
        control_function = fuzzy_logic_controller.create_control_function(control_input)
        control_output = fuzzy_logic_controller.calculate_centroid(
            display_range, control_function
        )
        if show_plot is True:
            plt.figure("final control function")
            plt.plot(
                display_range, control_function(display_range), label="control function"
            )
            plt.axvline(control_output, color="r", label=control_output, linestyle="--")
            plt.show()
        return control_output


if __name__ == "__main__":

    input_fuzzifier = {
        "low": create_normal_func(0, 1),
        "medium": create_normal_func(2.5, 1),
        "high": create_normal_func(5, 1),
    }

    output_fuzzifier = {
        "slow down": create_triangle_func(-2, -1, -0),
        "maintain speed": create_triangle_func(-1, 0, 1),
        "speed up": create_triangle_func(0, 1, 2),
    }

    input_output_links = {
        "low": "speed up",
        "medium": "maintain speed",
        "high": "slow down",
    }

    fuzzy_logic_controller = FuzzyLogicController(
        input_fuzzifier,
        output_fuzzifier,
        input_output_links,
    )

    control_range = np.arange(0, 5, 0.01)
    display_range = np.arange(-2, 2, 0.01)
    # step 1: create a control function at the current point.
    x_range = np.arange(0, 5, 0.1)
    output_shape = []
    for x in x_range:
        output = fuzzy_logic_controller.calculate_control_output(x, False)
        print(f"input: {x:2f} output: {output:2f}")
        output_shape.append(output)

    plt.figure("output shape")
    plt.plot(x_range, output_shape)
    plt.show()
