"""Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a 
farm. How many rabbits and how many chickens do we have?"""
def solve_puzzle():
    for rabbits in range(0, 36):  # Max 35 heads
        chickens = 35 - rabbits
        total_legs = 2 * chickens + 4 * rabbits
        if total_legs == 94:
            return chickens, rabbits

chickens, rabbits = solve_puzzle()
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
