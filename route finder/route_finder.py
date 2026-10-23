import sys
def finding_cost(x, y, grid, costs, record):
    if (x, y) in record:
        return record[(x, y)] #record is a dictionary to hold costs of the cells
    cost1, cost2, cost3 = costs
    rows, cols = len(grid), len(grid[0])
    if grid[x][y] == 0:#grid is a list that made of lists. each list in grid is a line in the input file.
        record[(x, y)] = 0
        return 0
    vertical_horizontal_neighbors = [(x - 1, y), (x + 1, y),(x, y - 1), (x, y + 1)]
    diagonal_neighbors = [(x - 1, y - 1), (x - 1, y + 1),(x + 1, y - 1), (x + 1, y + 1)]
    vertical_horizontal_sinkhole = False
    for nx, ny in vertical_horizontal_neighbors:
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            vertical_horizontal_sinkhole = True
            break # to check if there is a sinkhole in vertical or horizontal neighbours
    diagonal_sinkhole = False
    for nx, ny in diagonal_neighbors:
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            diagonal_sinkhole = True
            break # to check if there is a sinkhole in diagonal neighbours
    if vertical_horizontal_sinkhole:
        record[(x, y)] = cost3
        return cost3
    elif diagonal_sinkhole:
        record[(x, y)] = cost2
        return cost2
    else:
        record[(x, y)] = cost1
        return cost1
def find_path(x, y, grid, costs, path, visited, best_path, min_cost, memo):
    rows, cols = len(grid), len(grid[0])
    if y == cols - 1:
        path_cost = 0
        for px, py in path:
            path_cost += finding_cost(px, py, grid, costs, memo)
        if path_cost < min_cost[0]:
            # if new path is cheaper, it updates the min_cost and enrol new path to best_path
            min_cost[0] = path_cost
            best_path.clear()
            best_path.extend(path)
        return
    directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != 0:
            visited.add((nx, ny))
            path.append((nx, ny))#if a cell is inside grid borders,not visited before and not a sinkhole; it appends the cell to path and visited.
            current_cost = 0
            for px, py in path:
                current_cost += finding_cost(px, py, grid, costs, memo)#it finds the total cost that in a path
            if min_cost[0]<= current_cost:
                # if the cost at the current point reached so far is bigger than min_cost that founded before, it stops going through this path.
                path.pop()
                visited.remove((nx, ny))#if the cost at the current point reached so far is bigger than min_cost that founded before, it stops going through this path.
                continue
            find_path(nx, ny, grid, costs, path, visited, best_path, min_cost, memo) #use recursion to go to next cell
            path.pop()#if a path's lookup is completed, it removes the last cell to go back.
            visited.remove((nx, ny))#to remove this cell from visited to visit again in alternative paths.
def cheapest_path(grid, costs):
    rows, cols = len(grid), len(grid[0])
    best_path = []
    min_cost = [float('inf')] # set min_cost value to infinitive to compare correctly
    visited = set()
    memo = {}
    for start_row in range(rows):
        if grid[start_row][0] == 1: #if a row's first cell is not a sinkhole, it starts looking for a path
            visited.clear()# visited is cleared because a new path search has started
            visited.add((start_row, 0))
            find_path(start_row, 0, grid, costs, [(start_row, 0)], visited, best_path, min_cost, memo)
    if not best_path:
        return "There is no possible route!"
    output_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            new_row.append(str(cell))
        output_grid.append(new_row)#a new grid(output_grid) is created to be written to file
    for x, y in best_path:
        output_grid[x][y] = 'X' #to mark the cheapest path that founded
    output = f"Cost of the route: {min_cost[0]}\n"
    for i, row in enumerate(output_grid): #to write "output_grid" list in a structure that given in the input file
        output += " ".join(row)
        if i < len(output_grid) - 1:
            output += "\n"
    return output
def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, 'r') as file:
        line = file.readline()
        elements = line.split()
        int_elements = map(int, elements)
        costs = tuple(int_elements)
        grid = []
        for line in file:
            elements = line.split()
            int_elements_list = list(map(int, elements))
            grid.append(int_elements_list)
    result = cheapest_path(grid, costs)
    with open(output_file, 'w') as file:
        file.write(result)
if __name__ == "__main__":
    main()










