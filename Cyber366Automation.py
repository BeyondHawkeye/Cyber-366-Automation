import os
import subprocess

def run_strings_on_file(input_file, output_file):
    # Run the strings command
    try:
        result = subprocess.run(
            ["strings", input_file],
            capture_output=True, 
            text=True,
            errors="ignore"
        )
        
        # Save output to text file
        with open(output_file, "w", encoding="utf-8", errors="ignore") as f:
            f.write(result.stdout)
        
        print(f"[+] Extracted strings from {input_file} -> {output_file}")
    except Exception as e:
        print(f"[!] Failed to process {input_file}: {e}")

def main():
    folder = os.getcwd()  # Current folder
    script_name = os.path.basename(__file__)

    for filename in os.listdir(folder):
        # Skip folders and the script itself
        if not os.path.isfile(filename) or filename == script_name:
            continue

        # Input file
        input_path = os.path.join(folder, filename)

        # Output file: example → sample.exe -> sample.exe_strings.txt
        output_path = os.path.join(folder, f"{filename}_strings.txt")

        run_strings_on_file(input_path, output_path)

if __name__ == "__main__":
    main()
