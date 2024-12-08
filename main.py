x = (
    0b000,
    0b001,
    0b010,
    0b011,
    0b100,
    0b101,
    0b110,
    0b111,
)

f = (
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    1
)

g = (
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
)

def compute_linearity(x, f, verbose = False):
    combinations = len(x) ** 2
    linear_fails = 0
    zero_count = 0

    for i, x_i in enumerate(x):
        for j, x_j in enumerate(x):
            x_ij = x_i ^ x_j

            k = next(k for k, x_ in enumerate(x) if x_ == x_ij)

            if f[i] ^ f[j] != f[k]:
                linear_fails += 1

                if verbose:
                    print("fail at:", f"f({bin(x_i)[2:].zfill(3)}) = {f[i]},", f"f({bin(x_j)[2:].zfill(3)}) = {f[j]},", f"f({bin(x_i)[2:].zfill(3)} + {bin(x_j)[2:].zfill(3)}) = {f[i] ^ f[j]} != {f[k]}")

            if f[k] ^ f[j] == 0:
                zero_count += 1

    is_linear = (linear_fails == 0)

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("is_linear:", is_linear)
    print("linear_fails:", linear_fails)
    print("combinations:", combinations)
    print("probability:", linear_fails / combinations)
    if not is_linear:
        print("zero_count:", zero_count)
        print("ones_count:", combinations - zero_count)
        if zero_count >= combinations / 2:
            print("g(_) = 0")
        else:
            print("g(_) = 1")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

compute_linearity(x, f, verbose = False)
compute_linearity(x, g, verbose = False)
