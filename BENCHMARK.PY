import subprocess
import logging

def benchmark_gpu():
    """Benchmark Hashcat on available GPUs."""
    try:
        subprocess.run(['hashcat', '-b'], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error benchmarking GPU: {e}")

if __name__ == "__main__":
    benchmark_gpu()
