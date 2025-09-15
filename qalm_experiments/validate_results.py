import multiprocessing
from equiv_verification import monte_carlo_compare_by_filename

def tester(arguments):
    circuit_name = arguments[0]
    interval = arguments[1]
    initial_file = f"circuit/nam_circs/{circuit_name}.qasm"
    optimized_file = f"../full_results/fresh_results/qalm_bench/nam/qalm/{circuit_name}_interval_{interval}_timeout_3600_result_circuit.qasm"
    if monte_carlo_compare_by_filename(initial_file, optimized_file):
        print(f"Test Passed for {circuit_name} with interval {interval}")
    else:
        print(f"!!!!!!!!!!!!!!!! FAILURE for {circuit_name} with interval {interval} !!!!!!!!!!!!!!!!!!!!!")

def validate_results():
    circuit_list = [("circuit/nam_circs/adder_8.qasm", "adder_8"),
                ("circuit/nam_circs/barenco_tof_3.qasm", "barenco_tof_3"),
                ("circuit/nam_circs/barenco_tof_4.qasm", "barenco_tof_4"),
                ("circuit/nam_circs/barenco_tof_5.qasm", "barenco_tof_5"),
                ("circuit/nam_circs/barenco_tof_10.qasm", "barenco_tof_10"),
                ("circuit/nam_circs/csla_mux_3.qasm", "csla_mux_3"),
                ("circuit/nam_circs/gf2^4_mult.qasm", "gf2^4_mult"),
                ("circuit/nam_circs/gf2^5_mult.qasm", "gf2^5_mult"),
                ("circuit/nam_circs/gf2^6_mult.qasm", "gf2^6_mult"),
                ("circuit/nam_circs/gf2^7_mult.qasm", "gf2^7_mult"),
                ("circuit/nam_circs/gf2^8_mult.qasm", "gf2^8_mult"),
                ("circuit/nam_circs/gf2^9_mult.qasm", "gf2^9_mult"),
                ("circuit/nam_circs/gf2^10_mult.qasm", "gf2^10_mult"),
                ("circuit/nam_circs/mod5_4.qasm", "mod5_4"),
                ("circuit/nam_circs/mod_mult_55.qasm", "mod_mult_55"),
                ("circuit/nam_circs/mod_red_21.qasm", "mod_red_21"),
                ("circuit/nam_circs/qcla_adder_10.qasm", "qcla_adder_10"),
                ("circuit/nam_circs/qcla_com_7.qasm", "qcla_com_7"),
                ("circuit/nam_circs/qcla_mod_7.qasm", "qcla_mod_7"),
                ("circuit/nam_circs/rc_adder_6.qasm", "rc_adder_6"),
                ("circuit/nam_circs/tof_3.qasm", "tof_3"),
                ("circuit/nam_circs/tof_4.qasm", "tof_4"),
                ("circuit/nam_circs/tof_5.qasm", "tof_5"),
                ("circuit/nam_circs/tof_10.qasm", "tof_10"),
                ("circuit/nam_circs/vbe_adder_3.qasm", "vbe_adder_3"),
                ];

    arguments = []
    interval_list = [0,1,5,50,100]
    for circuit in circuit_list:
        for interval in interval_list:
            arguments.append((circuit[1], interval))

    with multiprocessing.Pool(50) as pool:
        pool.map(tester, arguments)

if __name__ == '__main__':
    validate_results()
