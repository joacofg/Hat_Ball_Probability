# Hat_Ball_Probability
Overview
The Hat Probability Simulator is a project that demonstrates the principles of probability and statistics using object-oriented programming in Python. This project simulates the drawing of balls from a hat to estimate probabilities of specific outcomes. It includes a Hat class to manage the balls in the hat and an experiment function to perform a large number of trials, thereby approximating the probability of drawing particular combinations of balls.

Features
Hat Class
The Hat class allows for the flexible initialization and management of a collection of balls:

Initialization: Create a hat with a variable number of balls of different colors. For example, Hat(red=3, blue=2, green=6).

Contents: Internally store the balls as a list of strings, where each string represents a ball of a specific color.

Draw Method: Simulate drawing a specified number of balls from the hat. The balls are drawn randomly and are not replaced, emulating an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls and empty the hat.

Experiment Function
The experiment function performs a series of trials to estimate the probability of drawing a specified combination of balls:

Parameters:

hat: A Hat object containing the balls.

expected_balls: A dictionary specifying the group of balls to attempt to draw (e.g., {'red':2, 'blue':1}).

num_balls_drawn: The number of balls to draw in each experiment.

num_experiments: The number of experiments to perform.

Process:

Copy the hat and perform the specified number of draws for each experiment.

Check if the drawn balls meet the expected criteria.

Calculate the probability as the ratio of successful experiments to total experiments.

Purpose
This project serves as an educational tool to demonstrate probability estimation through simulation. It also showcases the practical application of object-oriented programming concepts in Python.

Conclusion
The Hat Probability Simulator offers a hands-on way to explore the principles of probability and statistics. By running multiple simulations, it provides a clear and practical understanding of how probabilities can be estimated in real-world scenarios. This project is perfect for students, educators, and anyone interested in the fascinating world of probabilities.
