import argparse
import subprocess
import os

def run_experiments(circuit_list_file):
    circuit_files = []
    with open(circuit_list_file, 'r') as f:
        for circuit_name in f:
            circuit_files.append(circuit_name)


    results = {}

    for circuit_file in circuit_files:
        res = subprocess.run(["./roqc/target/release/roqc", circuit_file.strip()], capture_output = True, text = True)
        final_length = 0
        for line in res.stdout.splitlines():
            if "Optimized length: " in line:
                final_length = int(line.strip().split()[-1])
        results[circuit_file] = final_length
    
    print(results)

    # Repeat
    for circuit_file in circuit_files:
        res = subprocess.run(["./roqc/target/release/roqc", circuit_file.strip() + ".roqc"], capture_output = True, text = True)
        final_length = 0
        for line in res.stdout.splitlines():
            if "Optimized length: " in line:
                final_length = int(line.strip().split()[-1])
                if results[circuit_file] == final_length:
                    circuit_files.remove(circuit_file)
                else:
                    print(f"Found additional improvement for {circuit_file}:", results[circuit_file], "->", final_length)
                    results[circuit_file] = final_length

    print(results)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")

    args = parser.parse_args()

    print(args.filename)

    run_experiments(args.filename)
