class ListComparer():
    def calculate_distance(self, x: list[int], y: list[int]) -> int:
        x.sort()
        y.sort()

        total_distance: int = 0

        for index, x_item in enumerate(x): # Assumes x and y have the same length
            position_distance = abs(x_item - y[index])
            total_distance = total_distance + position_distance

        return total_distance

if __name__ == "__main__":
    print("implement me")