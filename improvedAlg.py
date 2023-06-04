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

    def __lt__(self, other):
        return self.x1 < other.x1

def bruteForceSolveVertAdjacencies(myList):
    rectanglesadjs = []
    for i, rect in enumerate(myList):
        adjs = []
        for adj_rect in myList:
            if rect.x2 == adj_rect.x1 and rect != adj_rect:
                adjs.append(adj_rect)
        rectangle_info = f"{i+1}, {len(adjs)}"
        for adj_rect in adjs:
            rectangle_info += f", {myList.index(adj_rect) + 1}, {adj_rect.x1}, {adj_rect.y1}, {adj_rect.x2}, {adj_rect.y2}"
        rectanglesadjs.append(rectangle_info)
    return rectanglesadjs


def lineSweepSolveVertAdjacencies(rectangles):
    events = SortedList()
    adjacency_list = defaultdict(list)

    # Create events
    for rect in rectangles:
        events.add((rect.x1, 'left', rect))
        events.add((rect.x2, 'right', rect))

    active_rectangles = set()
    y_coords = set()
    rectanglesadjs = []

    # Process events
    for event in events:
        x, event_type, rect = event

        if event_type == 'left':
            active_rectangles.add(rect)
            y_coords.add(rect.y1)
            y_coords.add(rect.y2)

            # Check for vertical adjacency with active rectangles
            for y_coord in y_coords:
                adj_rects = [
                    adj_rect
                    for adj_rect in active_rectangles
                    if adj_rect.y2 == y_coord and adj_rect != rect
                ]
                adjacency_list[rect].extend(adj_rects)
                adjacency_list.update(
                    {
                        adj_rect: [rect]
                        for adj_rect in adj_rects
                    }
                )

        else:
            active_rectangles.remove(rect)

    # Construct adjacency information
    for rect in rectangles:
        adj_info = f"{rectangles.index(rect) + 1}, "
        adj_rects = adjacency_list[rect]
        adj_info += f"{len(adj_rects)}, "
        for adj_rect in adj_rects:
            adj_info += f"{rectangles.index(adj_rect) + 1}, {adj_rect.x1}, {adj_rect.y1}, {adj_rect.x2}, {adj_rect.y2}, "
        rectanglesadjs.append(adj_info)

    return rectanglesadjs


def generate_rectangles(num_rectangles):
    xb = 1
    yb = 1
    max_range = 10
    rectangles = []
    for i in range(num_rectangles):
        xa = random.randint(0, max_range)
        ya = random.randint(0, max_range)
        width = random.randint(1, max_range)
        height = random.randint(1, max_range)
        rectangles.append(Rectangle(xa, ya, xa + width, ya + height))
    return rectangles


# Comparison plot
num_rectangles = [200, 400, 600, 800, 1000, 1100]
brute_force_times = []
line_sweep_times = []

for num in num_rectangles:
    rectangles = generate_rectangles(num)

    start_time = time.time()
    bruteForceSolveVertAdjacencies(rectangles)
    brute_force_times.append(time.time() - start_time)

    start_time = time.time()
    lineSweepSolveVertAdjacencies(rectangles)
    line_sweep_times.append(time.time() - start_time)

# Plotting
plt.plot(num_rectangles, brute_force_times, label='Brute Force')
plt.plot(num_rectangles, line_sweep_times, label='Line Sweep')
plt.xlabel('Number of Rectangles')
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Execution Time')
plt.legend()
plt.grid(True)
plt.savefig('execution_time_vs_rectangles.pdf')