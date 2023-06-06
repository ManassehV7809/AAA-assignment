import matplotlib.pyplot as plt
import numpy as np
import random
import time
from collections import defaultdict
from sortedcontainers import SortedList


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def intersects(self, other):
        return not (self.x2 <= other.x1 or other.x2 <= self.x1 or self.y2 <= other.y1 or other.y2 <= self.y1)

    def __lt__(self, other):
        return self.x1 < other.x1


def lineSweepSolveHorizAdjacencies(rectangles):
    events = []
    adjacency_list = defaultdict(list)

    # Create events
    for rect in rectangles:
        events.append((rect.y1, 'bottom', rect))
        events.append((rect.y2, 'top', rect))

    active_rectangles = set()

    # Process events
    events.sort()  # Sort events by y-coordinate

    for event in events:
        y, event_type, rect = event

        if event_type == 'bottom':
            active_rectangles.add(rect)

            # Check for horizontal adjacency with active rectangles
            for adj_rect in active_rectangles:
                if rect.y2 == adj_rect.y1:  # Check if the top edge of rect matches the bottom edge of adj_rect
                    adjacency_list[rect].append(adj_rect)
                    adjacency_list[adj_rect].append(rect)

        else:
            active_rectangles.remove(rect)

    # Construct adjacency information
    rectanglesadjs = []
    for rect in rectangles:
        adj_info = f"{rectangles.index(rect) + 1}, "
        adj_rects = adjacency_list[rect]
        adj_info += f"{len(adj_rects)}, "
        for adj_rect in adj_rects:
            adj_info += f"{rectangles.index(adj_rect) + 1}, "
        rectanglesadjs.append(adj_info)

    return rectanglesadjs


def generate_rectangles(num_rectangles, x_range, y_range):
    rectangles = []
    for _ in range(num_rectangles):
        while True:
            x1 = random.randint(x_range[0], x_range[1] - 1)
            y1 = random.randint(y_range[0], y_range[1] - 1)
            max_width = x_range[1] - x1
            max_height = y_range[1] - y1
            if max_width < 1 or max_height < 1:
                continue  # Skip generating rectangle if range is too small
            width = random.randint(1, max_width)
            height = random.randint(1, max_height)
            x2 = x1 + width
            y2 = y1 + height
            new_rect = Rectangle(x1, y1, x2, y2)
            if not any(rect.intersects(new_rect) for rect in rectangles):
                rectangles.append(new_rect)
                break
    return rectangles


def plot_rectangles(rectangles):
    fig, ax = plt.subplots()
    for rect in rectangles:
        x = [rect.x1, rect.x2, rect.x2, rect.x1, rect.x1]
        y = [rect.y1, rect.y1, rect.y2, rect.y2, rect.y1]
        ax.plot(x, y, 'b-')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Input Rectangles')
    plt.show()


def main():
    num_rectangles = 5
    x_range = (0, 15)
    y_range = (0, 15)

    rectangles = generate_rectangles(num_rectangles, x_range, y_range)
    plot_rectangles(rectangles)

    # Solve horizontal adjacencies using line sweep algorithm
    start_time = time.time()
    line_sweep_results = lineSweepSolveHorizAdjacencies(rectangles)
    line_sweep_time = time.time() - start_time

    print("Line Sweep Results:")
    for result in line_sweep_results:
        print(result)

    print("Line Sweep Execution Time:", line_sweep_time)


if __name__ == "__main__":
    main()
