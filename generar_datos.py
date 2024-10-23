import random
import os

def generate_dataset(size, filename):
    """Generate a dataset of given size and save it to a file."""
    with open(filename, 'w') as f:
        for _ in range(size):
            f.write(f"{random.randint(1, 1000000)}\n")

def main():
    # Ensure the datasets directory exists
    os.makedirs('datasets', exist_ok=True)

    # Define the sizes of datasets to generate
    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,
             20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

    # Generate datasets for each size
    for size in sizes:
        filename = f"datasets/data_{size}.txt"
        generate_dataset(size, filename)
        print(f"Generated dataset with {size} elements: {filename}")

if __name__ == "__main__":
    main()
    print("All datasets have been generated successfully.")