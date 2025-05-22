from random import shuffle, seed

class LatinSquareProblem():
    def __init__(self, n: int):
        self.n = n
        self.matrix = self.generate_initial_solution()
        self.print_square()

    def generate_initial_solution(self):
        initial_solution = [[] for _ in range(self.n)]
        numbers = []
        for i in range(self.n):
            for _ in range(self.n):
                numbers.append(i+1)
        shuffle(numbers)
        for i, number in enumerate(numbers):
            initial_solution[i // 5].append(number)

        return initial_solution
    
    def print_square(self):
        for y in range(self.n):
            for x in range(self.n):
                print(self.matrix[y][x], end=" ")
            print()



if __name__ == "__main__":
    seed(123)
    LatinSquareProblem(5)