import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_count = {color: drawn_balls.count(color) for color in expected_balls}
        success = all(drawn_count[color] >= expected_balls[color] for color in expected_balls)
        if success:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red': 2, 'green': 1}, num_balls_drawn=5, num_experiments=2000)
print(probability)  # Output: Approximate probability