from text_parser import preprocessor

line_groups = {}

with open('sample-file.txt', 'r') as f:
    for i, raw_line in enumerate(f, 1):
        clean_line = raw_line.strip()
        normalized = "".join(preprocessor(clean_line))
        if not normalized:
            continue
        if normalized not in line_groups:
            line_groups[normalized] = []
        line_groups[normalized].append((i, clean_line))

duplicate_sets = []
for key in line_groups:
    if len(line_groups[key]) > 1:
        duplicate_sets.append(line_groups[key])

print(f"There are {len(duplicate_sets)} sets.")

for group in duplicate_sets[:2]:
    print("\nset:")
    for line_num, original in group:
        print(f"line {line_num}: {original}")