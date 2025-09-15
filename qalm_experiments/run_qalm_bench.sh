# Adapted from run_all_tools.sh from QUOQ

# #!\bin\bash

benchmark=$1
timeout=$2
num_guoq_trials=$3
source tool_invoke_defs.sh

############################## Make fresh results dirs ##############################

mkdir -p fresh_results
mkdir -p fresh_results/qalm_bench

mkdir -p fresh_results/qalm_bench/nam
mkdir -p fresh_results/qalm_bench/nam/guoq
mkdir -p fresh_results/qalm_bench/nam/voqc
mkdir -p fresh_results/qalm_bench/nam/qiskit
mkdir -p fresh_results/qalm_bench/nam/queso
mkdir -p fresh_results/qalm_bench/nam/qalm

######## Running tests on Nam gate set"

BENCHMARK_DIR="qalm"
echo "Running experiments on qalm circuits with Nam gate set:"

for i in $(seq 1 $num_guoq_trials); do
    echo "Running GUOQ trial $i out of $num_guoq_trials on $benchmark..."
    guoq_args="-g!NAM!-opt!TOTAL!--rules-dir!/home/queso_rules/!--resynth-weight!180"
    run_guoq $BENCHMARK_DIR/$benchmark $timeout $guoq_args $i "--bqskit"
done
mv results_* fresh_results/qalm_bench/nam/guoq

run_qiskit $BENCHMARK_DIR/$benchmark $timeout "nam"
mv results_* fresh_results/qalm_bench/nam/qiskit

run_queso $BENCHMARK_DIR/$benchmark $timeout "-g!NAM!-opt!TOTAL!--rules-dir!/home/queso_rules/!-search!BEAM!-temp!0!-q!8000!-resynth!NONE"
mv results_* fresh_results/qalm_bench/nam/queso


run_voqc $BENCHMARK_DIR/$benchmark $timeout "nam"
mv results_* fresh_results/qalm_bench/nam/voqc
