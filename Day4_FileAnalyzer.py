# Day4_FileAnalyzer.py

file_path = input("Enter the file path to analyze: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        chars = len(content)

        print(f"\n📄 File Analysis for: {file_path}")
        print(f"Total Lines: {len(lines)}")
        print(f"Total Words: {len(words)}")
        print(f"Total Characters: {chars}")

except FileNotFoundError:
    print("⚠️ File not found. Check the path and try again.")
except Exception as e:
    print("Error:", e)
