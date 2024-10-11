# Step 1: Read the file
with open('telegram_urls.txt', 'r') as file:
    lines = file.readlines()

# Step 2: Remove duplicate lines
unique_lines = list(set(lines))

# Step 3: Sort the lines if order is important (optional)
unique_lines.sort()

# Step 4: Write the unique lines back to the file
with open('output.txt', 'w') as file:
    file.writelines(unique_lines)
