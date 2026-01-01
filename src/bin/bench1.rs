use rubixpy::{Permutation, *};

use std::time::{Duration, Instant};

fn main() {
    println!("Hello, World!");

    let start = Instant::now();
    let p = Permutation::new()
        .tn(TR, 2)
        .tn(TT, 2)
        .tn(TR, 2)
        .tn(TT, 2)
        .tn(TR, 2)
        .tn(TT, 2)
        .out();

    let result = init_search(p, hash_permutation(&BASE));
    println!("Elapsed: {} ms", start.elapsed().as_millis())
}
