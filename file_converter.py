import sys
import markdown

if len(sys.argv) != 4:
    print("Usage: python3 file_converter.py markdown inputfile outputfile")
    sys.exit(1)

command = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]

if command != "markdown":
    print("Unsupported command. Only 'markdown' is supported.")
    sys.exit(1)

try:
    with open(input_path, 'r') as f:
        md_text = f.read()

    html = markdown.markdown(md_text)

    with open(output_path, 'w') as f:
        f.write(html)

    print(f"Converted {input_path} to {output_path}")
except Exception as e:
    print(f"Error: {e}")
