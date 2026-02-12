from text_parser import find_lines_containing

results = find_lines_containing('sample-file.txt', 'lorem')

print(f"Total matching lines: {len(results)}")

print("\nFirst 3 matches:")
for line_num, text in results[:3]:
    print(f"Line {line_num}: {text}")