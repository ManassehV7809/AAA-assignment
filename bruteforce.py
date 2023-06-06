import matplotlib.pyplot as plt
import numpy as np
import random
from collections import defaultdict
from sortedcontainers import SortedList





def lineSweepSolveVertAdjacencies(rectangles):
    events = SortedList()
    adjacency_list = defaultdict(list)

    # Create events
    for rect in rectangles:
        events.add((rect.x2, 'right', rect))  # Change x1 to x2 for 'right' events

    active_rectangles = set()
    y_coords = set()
   
    # Process events
    for event in events:
        x, event_type, rect = event

        if event_type == 'right':  # Modify the condition for 'right' events
            active_rectangles.add(rect)
            y_coords.add(rect.y1)
            y_coords.add(rect.y2)

            # Check for vertical adjacency with active rectangles on the left
            for y_coord in y_coords:
                adj_rects = [
                    adj_rect
                    for adj_rect in active_rectangles
                    if adj_rect.x2 <= rect.x1 and adj_rect.y1 <= rect.y2 and adj_rect.y2 >= rect.y1
                ]
                adjacency_list[rect].extend(adj_rects)
                adjacency_list.update({adj_rect: [rect] for adj_rect in adj_rects})

            active_rectangles.remove(rect)  # Remove the rectangle from active_rectangles

    # Construct adjacency information
    rectanglesadjs = []
    for rect in rectangles:
        adj_info = f"{rectangles.index(rect) + 1}, "
        adj_rects = adjacency_list[rect]
        adj_info += f"{len(adj_rects)}, "
        for adj_rect in adj_rects:
            adj_info += f"{rectangles.index(adj_rect) + 1}, {adj_rect.x1}, {adj_rect.y1}, {adj_rect.x2}, {adj_rect.y2}, "
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
    print(rectangles)
    #plot_rectangles(rectangles)

    # Solve vertical adjacencies using line sweep algorithm
    line_sweep_results = lineSweepSolveVertAdjacencies(rectangles)

    print("Line Sweep Results:")
    for result in line_sweep_results:
        print(result)


if __name__ == "__main__":
    main()
