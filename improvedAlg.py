import matplotlib.pyplot as plt
import random
from collections import defaultdict
from sortedcontainers import SortedList

def lineSweepSolveVertAdjacencies(rectangles):
    events = SortedList()
    adjacency_list = defaultdict(list)

    # Create events
    for rect in rectangles:
        events.add((rect[0], 'left', rect))
        events.add((rect[2], 'right', rect))

    active_rectangles = set()

    # Process events
    for event in events:
        x, event_type, rect = event

        if event_type == 'left':
            for adj_rect in active_rectangles:
                if adj_rect[3] > rect[1] and adj_rect[1] < rect[3]:
                    adjacency_list[rect].append(adj_rect)

            active_rectangles.add(rect)

        elif event_type == 'right':
            active_rectangles.remove(rect)

    # Construct adjacency information
    rectanglesadjs = []
    for rect in rectangles:
        adj_info = f"{rectangles.index(rect) + 1}, "
        adj_rects = adjacency_list[rect]
        adj_info += f"{len(adj_rects)}, "
        for adj_rect in adj_rects:
            adj_info += f"{rectangles.index(adj_rect) + 1}, {adj_rect[0]}, {adj_rect[1]}, {adj_rect[2]}, {adj_rect[3]}, "
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
                continue
            width = random.randint(1, max_width)
            height = random.randint(1, max_height)
            x2 = x1 + width
            y2 = y1 + height
            new_rect = (x1, y1, x2, y2)
            if not any(rect_intersects(new_rect, rect) for rect in rectangles):
                rectangles.append(new_rect)
                break

    # Sort rectangles based on x-coordinate
    rectangles.sort(key=lambda rect: rect[0])
    return rectangles


def rect_intersects(rect1, rect2):
    return not (rect1[2] <= rect2[0] or rect2[2] <= rect1[0] or rect1[3] <= rect2[1] or rect2[3] <= rect1[1])


def plot_rectangles(rectangles):
    fig, ax = plt.subplots()
    for rect in rectangles:
        x = [rect[0], rect[2], rect[2], rect[0], rect[0]]
        y = [rect[1], rect[1], rect[3], rect[3], rect[1]]
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
    plot_rectangles(rectangles)

    # Solve vertical adjacencies using line sweep algorithm
    line_sweep_results = lineSweepSolveVertAdjacencies(rectangles)

    print("Line Sweep Results:")
    for result in line_sweep_results:
        print(result)


if __name__ == "__main__":
    main()
