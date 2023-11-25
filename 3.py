import random

population_size = 1000000
positive_percentage = 0.52
negative_percentage = 0.48
sample_sizes = [20, 100, 400]
num_experiments = 100
target_probability = 0.9

# Generate the population with +1 and -1 votes
population = [1] * int(population_size * positive_percentage) + [-1] * int(population_size * negative_percentage)

# Function to perform random sampling
def random_sampling(population, sample_size):
    return random.sample(population, sample_size)

# Function to calculate the probability of +1 being the majority in the sample
def calculate_probability(sample, majority_threshold=0.5):
    count_positive = sum(1 for vote in sample if vote == 1)
    return count_positive / len(sample) > majority_threshold

# Function to find the sample size needed for a given probability threshold
def find_required_sample_size(target_probability, population_size, positive_percentage):
    required_sample_size = 1
    while True:
        sample = random_sampling(population, required_sample_size)
        sample_probability = calculate_probability(sample)
        if sample_probability >= target_probability:
            break
        required_sample_size += 1
    return required_sample_size

# Run experiments for different sample sizes
for size in sample_sizes:
    success_count = 0
    for _ in range(num_experiments):
        sample = random_sampling(population, size)
        if calculate_probability(sample):
            success_count += 1
    probability = success_count / num_experiments
    print(f"Sample size: {size}, Probability of +1 being the majority: {probability}")

# Find the sample size needed for the target probability
required_size = find_required_sample_size(target_probability, population_size, positive_percentage)
print(f"\nTo achieve a probability of {target_probability}, you need a sample size of at least {required_size}.")
