from client import ConstantTimeCryptoValidator

def run_example():
    print("=== GenPark Constant-Time Comparator Example ===")
    val = ConstantTimeCryptoValidator()
    print("Result:", val.benchmark_constant_time_comparison())

if __name__ == "__main__":
    run_example()
