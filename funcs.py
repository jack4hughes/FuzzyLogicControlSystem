import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def fuzzy_and(*funcs):
    # Returns a function that ANDS all functions
    def return_function(value):
        return np.maximum.reduce([func(value) for func in funcs])

    return return_function


def fuzzy_or(*funcs):
    def return_function(value):
        return np.minimum.reduce([func(value) for func in funcs])

    return return_function


def create_clipped_func(func, max_value):
    def returned_func(value):
        return np.minimum(func(value), max_value)

    return returned_func


def create_normal_func(mean, std):
    gaussian = stats.norm(mean, std)
    normalisation_value = gaussian.pdf(mean)
    return lambda x: gaussian.pdf(x) / normalisation_value


def create_triangle_func(minimum, top, maximum):
    """This factory creates a triangle function, which is a standard function for the output of a fuzzy logic system.

    - top: The position of the top of the triangle function"""
    test_range = np.arange(-10, 10, 0.1)
    rising_edge_gradient = 1 / (top - minimum)
    falling_edge_gradient = 1 / (top - maximum)

    print(
        f"rising edge length: {rising_edge_gradient}\nfalling_edge_length: {falling_edge_gradient}"
    )

    # optimised claude code!

    def return_function(values):
        values = np.asarray(values)

        # Find rising and falling y_intercepts of triangle.
        y_intercept_rising = -rising_edge_gradient * minimum
        y_intercept_falling = -falling_edge_gradient * maximum

        # Create functions for rising and falling edges of triangle
        ramp_up = values * rising_edge_gradient + y_intercept_rising
        ramp_down = values * falling_edge_gradient + y_intercept_falling

        # combine rising and falling edges using minimum function
        triangle = np.minimum(ramp_up, ramp_down)

        # return 0 if outside of triangle.
        outputs = np.maximum(triangle, 0)

        # Return scalar if input was scalar (taken from claude.)
        return outputs.item() if outputs.size == 1 else outputs

    return_function(test_range)
    return return_function


if __name__ == "__main__":
    plt.figure("triangle test")
    tri_test_range = np.arange(-5, 5, 0.1)
    tri_func_1 = create_triangle_func(0, 2, 4)
    tri_func_2 = create_triangle_func(-4, -1, 0)
    tri_func_3 = create_triangle_func(2, 3, 4)
    
    plt.plot(tri_test_range, tri_func_1(tri_test_range), "--")
    plt.plot(tri_test_range, tri_func_2(tri_test_range), "--")
    plt.plot(tri_test_range, tri_func_3(tri_test_range), "--")
    plt.plot(tri_test_range, fuzzy_and(tri_func_1, tri_func_2, tri_func_3)(tri_test_range))


    plt.figure("gaussian Test")
    func_1 = create_normal_func(1, 0.2)
    func_2 = create_normal_func(0, 4)
    func_3 = create_normal_func(-1,3)
    fuzzy_or_result = fuzzy_or(func_1, func_2, func_3)

    plt.plot(tri_test_range, func_1(tri_test_range), "--")
    plt.plot(tri_test_range, func_2(tri_test_range), "--")
    plt.plot(tri_test_range, func_3(tri_test_range), "--")
    plt.plot(tri_test_range, fuzzy_or_result(tri_test_range))
    plt.show()
