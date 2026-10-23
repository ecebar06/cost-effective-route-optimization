# Cost-Effective Route Optimization

An optimized pathfinding engine implemented in Python to discover the least-cost route across grid networks with dynamic obstacles and neighbor-dependent cost rules.

## Features

- **Pathfinding Engine:** Computes optimal paths from the leftmost to the rightmost column of a weighted grid using recursive backtracking.
- **Dynamic Cell Cost Calculation:** Evaluates neighbor states (sinkholes/obstacles) to assign dynamic movement costs.
- **Memoization & Caching:** Uses dictionary-based memoization to cache calculated cell costs and reduce redundant neighbor lookups.
- **Search Space Pruning:** Halts recursive paths early if the accumulated cost exceeds the currently known minimum cost.
- **Path Visualizer & Report Generator:** Marks the optimal path directly on the grid output with 'X' identifiers and calculates total traversal metrics.

## Tech Stack

- **Language:** Python 3.x
- **Core Concepts:** Recursion, Backtracking, Memoization, Search Space Pruning, Grid Search Algorithms

## How to Run

Run the pathfinder with input grid and output text paths:
python route_finder.py input_grid.txt output_route.txt
