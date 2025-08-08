import json
import csv

class OptResult:
    def __init__(self, initial_count, final_count):
        self.initial_gate_count = float(initial_count)
        self.final_gate_count = float(final_count)

    def __repr__(self):
        return f"(Original length: {self.initial_gate_count}, Final length: {self.final_gate_count})"

def collect_qualm_results():
    pass

def process_results():
    circuit_list = []

    total_results = {}

    total_results["qualm_1_results"] = []
    total_results["qualm_5_results"] = []
    total_results["qualm_50_results"] = []
    total_results["qualm_100_results"] = []
    total_results["quartz_results"] = []
    total_results["voqc_results"] = []
    total_results["qiskit_results"] = []
    total_results["guoq_results"] = []
    total_results["queso_results"] = []
    
    with open("qualm_circuits_test.txt", "r") as f:
        circuit_list = [line.split("/")[-1].strip().split(".")[0] for line in f.readlines()]

    collect_qualm_results()

    results_file = "qualm_bench_results.csv"

    for circuit in circuit_list:

        for res in parse_qualm_quartz_voqc(circuit):
            total_results[res[0] + "_results"].append(res[1])

        r_queso = parse_queso(circuit)
        r_guoq = parse_guoq(circuit)
        r_qiskit = parse_qiskit(circuit)


        total_results["qiskit_results"].append(r_qiskit)
        total_results["guoq_results"].append(r_guoq)
        total_results["queso_results"].append(r_queso)

    opt_order = ["qualm_1", "qualm_5","qualm_50", "qualm_100", "quartz", "voqc", "qiskit", "guoq", "queso"]

    fields = ["Optimizer Name"] + circuit_list
    all_data = []

    # Put original gate count in:
    original_lengths = ["initial"] + [r.initial_gate_count for r in total_results["qiskit_results"]]

    for opt_method in opt_order:
        opt_data = [opt_method]
        for result in total_results[opt_method + "_results"]:
            opt_data.append(result.final_gate_count)
        all_data.append(opt_data)

    with open(results_file, 'w') as r_out:
        csv_writer = csv.writer(r_out)
        csv_writer.writerow(fields)
        csv_writer.writerow(original_lengths)
        csv_writer.writerows(all_data)


# These results come from own experiments
def parse_qualm_quartz_voqc(circuit_name):
    with open(f"fresh_results/qualm_bench/nam/qualm/results_{circuit_name}.txt", "r") as f:
        for line in f.readlines():
            words = line.split()
            counts = words[1].split("/")
            yield (words[0], OptResult(counts[0], counts[1]))

# These results come from guoq artifact code
# TODO: Check that parameters are correct: none_none vs none_1 also optimization goal
def parse_guoq(circuit_name):
    result_file = f"fresh_results/qualm_bench/nam/guoq/results_{circuit_name}/results_none_1.json"
    with open(result_file, "r") as f:
        result_dict = json.load(f)
        results = OptResult(result_dict["original_total"], result_dict["best_circuit_size"])
    return results

def parse_queso(circuit_name):
    result_file = f"fresh_results/qualm_bench/nam/queso/results_{circuit_name}/results_none_none.json"
    with open(result_file, "r") as f:
        result_dict = json.load(f)
        results = OptResult(result_dict["original_total"], result_dict["best_circuit_size"])
    return results

def parse_qiskit(circuit_name):
    result_file = f"fresh_results/qualm_bench/nam/qiskit/results_{circuit_name}/results_none_none.json"
    with open(result_file, "r") as f:
        result_dict = json.load(f)
        results = OptResult(result_dict["original_total"], result_dict["optimized_total"])
    return results


if __name__ == '__main__' :
    process_results()
