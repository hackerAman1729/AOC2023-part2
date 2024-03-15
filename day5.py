filePath = 'input/aoc2023day5.txt'

def convert_number(num, dest_map):
    for dest_start, source_start, length in dest_map:
        if source_start <= num < source_start + length:
            return dest_start + (num - source_start)
    return num

data = {}
seeds = []

with open(filePath) as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()

        if line.startswith('seeds:'):
            seeds = [int(x) for x in line.split(': ')[1].split()]

        elif line:
            if line.endswith(":"):
                current_key = line[:-1]
                data[current_key] = []
                current_list = data[current_key]
            else:
                current_list.append([int(x) for x in line.split()])


# for i in range(0, len(seeds), 2):
#     start = seeds[i]
#     count = seeds[i+1]
#     seeds.extend(range(start, start + count))

print(seeds)

maps = {
    'seed-to-soil map': data['seed-to-soil map'],
    'soil-to-fertilizer map': data['soil-to-fertilizer map'],
    'fertilizer-to-water map': data['fertilizer-to-water map'],
    'water-to-light map': data['water-to-light map'],
    'light-to-temperature map': data['light-to-temperature map'],
    'temperature-to-humidity map': data['temperature-to-humidity map'],
    'humidity-to-location map': data['humidity-to-location map']
}

lowest_location = float('inf')
for seed in seeds:
    current_num = seed
    for _, dest_map_name in [
        ('seeds', 'seed-to-soil map'),
        ('seed-to-soil map', 'soil-to-fertilizer map'),
        ('soil-to-fertilizer map', 'fertilizer-to-water map'),
        ('fertilizer-to-water map', 'water-to-light map'),
        ('water-to-light map', 'light-to-temperature map'),
        ('light-to-temperature map', 'temperature-to-humidity map'),
        ('temperature-to-humidity map', 'humidity-to-location map')
    ]:
        # Convert using only the destination map
        current_num = convert_number(current_num, maps[dest_map_name])
    lowest_location = min(lowest_location, current_num)

print(f"Lowest location number: {lowest_location}")