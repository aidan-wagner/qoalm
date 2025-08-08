FROM amxu/guoq:1

WORKDIR /home

RUN apt-get update && apt-get install git

RUN rm -r /home/quartz

# RUN git clone https://github.com/aidan-wagner/qoalm.git

# COPY qualm_circuits.txt start_qualm_bench.sh run_on_qualm_circuits.sh /home/

# COPY testing_qualm_light.txt testing_qualm_bench.sh /home/

COPY . /home/qualm

RUN mv qualm/run_qualm_bench.sh /home/
RUN mv qualm/qualm_bench_test.sh /home/
RUN mv qualm/qualm_bench_full.sh /home/
RUN mv qualm/qualm_circuits_test.txt /home/
RUN mv qualm/qualm_circuits_full.txt /home/
RUN mv qualm/compile_results.py /home/

# Enable Executables
RUN chmod +x run_qualm_bench.sh
RUN chmod +x qualm_bench_test.sh
RUN chmod +x qualm_bench_full.sh

# Install Rust - Doesn't work
# RUN curl -y --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install Python Dependencies
RUN pip install matplotlib qiskit
RUN pip install pybind11[global]
