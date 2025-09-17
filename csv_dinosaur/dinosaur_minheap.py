#!/usr/bin/env python3

''' 
Interview Follow-ups: 
1. One file small, one large: Load small file in memory, stream large file 
2. Both files large: Use external sorting or MapReduce 
3. Empty files: Check file existence and size before processing 
4. Frequent updates: Implement caching with file modification time checks 
'''

import csv
import math
import heapq
import sys

G = 9.8  # gravitational constant

# Parse CSV and return {name: value} for the relevant column.
def parse_csv(filename, filter_bipedal=False):
    
    data = {}
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if filter_bipedal and row.get("STANCE") != "bipedal":
                continue
            name = row.get("NAME")
            if not name:
                continue
            try:
                if "LEG_LENGTH" in row and row["LEG_LENGTH"]:
                    data[name] = float(row["LEG_LENGTH"])
                elif "STRIDE_LENGTH" in row and row["STRIDE_LENGTH"]:
                    data[name] = float(row["STRIDE_LENGTH"])
            except ValueError:
                # Skip only the bad row; do not print anything
                continue
    return data

def calculate_dinosaur_speeds(file1, file2):
    leg_lengths = parse_csv(file1)
    stride_lengths = parse_csv(file2, filter_bipedal=True)

    speed_heap = []  # max-heap via negative keys
    for name, stride_length in stride_lengths.items():
        leg_length = leg_lengths.get(name)
        if leg_length is None or leg_length == 0:
            continue
        ratio = stride_length / leg_length
        speed = (ratio - 1.0) * math.sqrt(leg_length * G)
        # If you want to exclude non-positive speeds, uncomment:
        # if speed <= 0: continue
        heapq.heappush(speed_heap, (-speed, name))

    result = []
    while speed_heap:
        _, name = heapq.heappop(speed_heap)
        result.append(name)
    return result

if __name__ == "__main__":
    # Use filenames from args or defaults
    file1 = sys.argv[1] if len(sys.argv) > 1 else "dataset1.csv"
    file2 = sys.argv[2] if len(sys.argv) > 2 else "dataset2.csv"
    for name in calculate_dinosaur_speeds(file1, file2):
        print(name)
