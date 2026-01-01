#![feature(test)]
extern crate test;

use itertools::Itertools;
use pyo3::prelude::*;

type Index = u8;
const RSIZE: usize = 54;
type PermutationRepr = [Index; RSIZE];

#[rustfmt::skip]
pub const BASE: PermutationRepr = [
    0, 1, 2, 3, 4, 5, 6, 7, 8,
    9,10,11,12,13,14,15,16,17,
    18,19,20,21,22,23,24,25,26,
    27,28,29,30,31,32,33,34,35,
    36,37,38,39,40,41,42,43,44,
    45,46,47,48,49,50,51,52,53,
];

#[rustfmt::skip]
pub const TS: PermutationRepr = [
    18,19,20,21,22,23,24,25,26,
    11,14,17,10,13,16,9,12,15,
    27,28,29,30,31,32,33,34,35,
    45,46,47,48,49,50,51,52,53, 
    42,39,36,43,40,37,44,41,38,
    0, 1, 2, 3, 4, 5, 6, 7, 8,
];

#[rustfmt::skip]
pub const TSI: PermutationRepr = [
    18,19,20,21,22,23,24,25,26,
    11,14,17,10,13,16, 9,12,15,
    27,28,29,30,31,32,33,34,35,
    45,46,47,48,49,50,51,52,53,
    42,39,36,43,40,37,44,41,38,
    0, 1, 2, 3, 4, 5, 6, 7, 8,
];

#[rustfmt::skip]
pub const TR: PermutationRepr = [
    0, 1,38, 3, 4,41, 6, 7,44,
    9,10, 2,12,13, 5,15,16, 8,
    18,19,20,21,22,23,24,25,26,
    17,28,29,14,31,32,11,34,35,
    36,37,33,39,40,30,42,43,27,
    51,48,45,52,49,46,53,50,47,
];

#[rustfmt::skip]
pub const TRI: PermutationRepr = [
   0, 1,11, 3, 4,14, 6, 7,17,
   9,10,33,12,13,30,15,16,27,
  18,19,20,21,22,23,24,25,26,
  44,28,29,41,31,32,38,34,35,
  36,37, 2,39,40, 5,42,43, 8,
  47,50,53,46,49,52,45,48,51,
];

#[rustfmt::skip]
pub const TF: PermutationRepr = [
   6, 3, 0, 7, 4, 1, 8, 5, 2,
   9,10,11,12,13,14,26,23,20,
  18,19,36,21,22,37,24,25,38,
  27,28,29,30,31,32,33,34,35,
  51,48,45,39,40,41,42,43,44,
  15,46,47,16,49,50,17,52,53,
];

#[rustfmt::skip]
pub const TFI: PermutationRepr = [
   2, 5, 8, 1, 4, 7, 0, 3, 6,
   9,10,11,12,13,14,45,48,51,
  18,19,17,21,22,16,24,25,15,
  27,28,29,30,31,32,33,34,35,
  20,23,26,39,40,41,42,43,44,
  38,46,47,37,49,50,36,52,53,
];

#[rustfmt::skip]
pub const TL: PermutationRepr = [
   9, 1, 2,12, 4, 5,15, 7, 8,
  35,10,11,32,13,14,29,16,17,
  24,21,18,25,22,19,26,23,20,
  27,28,42,30,31,39,33,34,36,
   0,37,38, 3,40,41, 6,43,44,
  45,46,47,48,49,50,51,52,53,
];

#[rustfmt::skip]
pub const TLI: PermutationRepr = [
  36, 1, 2,39, 4, 5,42, 7, 8,
   0,10,11, 3,13,14, 6,16,17,
  20,23,26,19,22,25,18,21,24,
  27,28,15,30,31,12,33,34, 9,
  35,37,38,32,40,41,29,43,44,
  45,46,47,48,49,50,51,52,53,
];

#[rustfmt::skip]
pub const TB: PermutationRepr = [
   0, 1, 2, 3, 4, 5, 6, 7, 8,
  47,50,53,12,13,14,15,16,17,
  11,19,20,10,22,23, 9,25,26,
  33,30,27,34,31,28,35,32,29,
  36,37,38,39,40,41,18,21,24,
  45,46,44,48,49,43,51,52,42,
];

#[rustfmt::skip]
pub const TBI: PermutationRepr = [
   0, 1, 2, 3, 4, 5, 6, 7, 8,
  24,21,18,12,13,14,15,16,17,
  42,19,20,43,22,23,44,25,26,
  29,32,35,28,31,34,27,30,33,
  36,37,38,39,40,41,53,50,47,
  45,46, 9,48,49,10,51,52,11,
];

#[rustfmt::skip]
pub const TD: PermutationRepr = [
   0, 1, 2, 3, 4, 5,24,25,26,
   9,10,11,12,13,14,15,16,17,
  18,19,20,21,22,23,33,34,35,
  27,28,29,30,31,32,51,52,53,
  42,39,36,43,40,37,44,41,38,
  45,46,47,48,49,50, 6, 7, 8,
];

#[rustfmt::skip]
pub const TDI: PermutationRepr = [
   0, 1, 2, 3, 4, 5,51,52,53,
   9,10,11,12,13,14,15,16,17,
  18,19,20,21,22,23, 6, 7, 8,
  27,28,29,30,31,32,24,25,26,
  38,41,44,37,40,43,36,39,42,
  45,46,47,48,49,50,33,34,35,
];

#[rustfmt::skip]
pub const TT: PermutationRepr = [
  45,46,47, 3, 4, 5, 6, 7, 8,
  15,12, 9,16,13,10,17,14,11,
   0, 1, 2,21,22,23,24,25,26,
  18,19,20,30,31,32,33,34,35,
  36,37,38,39,40,41,42,43,44,
  27,28,29,48,49,50,51,52,53,
];

#[rustfmt::skip]
pub const TTI: PermutationRepr = [
  18,19,20, 3, 4, 5, 6, 7, 8,
  11,14,17,10,13,16, 9,12,15,
  27,28,29,21,22,23,24,25,26,
  45,46,47,30,31,32,33,34,35,
  36,37,38,39,40,41,42,43,44,
   0, 1, 2,48,49,50,51,52,53,
];

// #[rustfmt::skip]
// const TSI: PermutationRepr

pub fn permute(a: &PermutationRepr, b: &PermutationRepr) -> PermutationRepr {
    (0..RSIZE)
        .map(|i| a[b[i] as usize])
        .collect_array()
        .unwrap()
}

pub struct Permutation([u8; RSIZE]);

impl Permutation {
    pub fn new() -> Self {
        Self(BASE)
    }

    pub fn t(mut self, b: PermutationRepr) -> Self {
        self.0 = permute(&self.0, &b);
        self
    }

    pub fn tn(mut self, b: PermutationRepr, n: usize) -> Self {
        for _ in 0..n {
            self = self.t(b);
        }
        self
    }

    pub fn out(self) -> PermutationRepr {
        self.0
    }
}

use std::char::MAX;
use std::cmp;
use std::collections::{HashMap, HashSet, VecDeque};

use std::hash::{DefaultHasher, Hash, Hasher};

const MAX_DEPTH: i32 = 5;

pub fn hash_permutation(p: &PermutationRepr) -> u64 {
    let mut hasher = DefaultHasher::new();
    p.hash(&mut hasher);
    hasher.finish()
}

fn get_adjacent_permutations(a: &PermutationRepr) -> [PermutationRepr; 12] {
    [
        permute(a, &TR),
        permute(a, &TL),
        permute(a, &TF),
        permute(a, &TD),
        permute(a, &TT),
        permute(a, &TB),
        permute(a, &TRI),
        permute(a, &TLI),
        permute(a, &TFI),
        permute(a, &TDI),
        permute(a, &TTI),
        permute(a, &TBI),
    ]
}

pub fn init_search(curr: PermutationRepr, target_hash: u64) -> Option<i32> {
    let mut visited: HashMap<u64, i32> = HashMap::new();
    visited.insert(hash_permutation(&curr), 0);
    let result = search(&mut visited, VecDeque::from([curr]), target_hash);

    if let Some(result) = result {
        return Some(result);
    }

    let mut visited2: HashMap<u64, i32> = HashMap::new();
    visited2.insert(hash_permutation(&BASE), 0);
    search(
        &mut visited2,
        VecDeque::from([BASE]),
        hash_permutation(&curr),
    );

    let visited_set_1: HashSet<u64> = HashSet::from_iter(visited.keys().map(|i| *i));
    let visited_set_2: HashSet<u64> = HashSet::from_iter(visited2.keys().map(|i| *i));
    let intersection = visited_set_1
        .intersection(&visited_set_2)
        .collect::<Vec<_>>();

    if intersection.len() == 0 {
        return None;
    }

    Some(
        intersection
            .into_iter()
            .map(|i| visited.get(i).unwrap() + visited2.get(i).unwrap())
            .min()
            .unwrap(),
    )
}

pub fn search(
    visited: &mut HashMap<u64, i32>,
    mut queue: VecDeque<PermutationRepr>,
    target_hash: u64,
) -> Option<i32> {
    while queue.len() > 0 {
        let curr = queue.pop_front().unwrap();
        let curr_hash = hash_permutation(&curr);
        if let Some(d) = visited.get(&curr_hash) {
            if *d > MAX_DEPTH {
                continue;
            }
        }
        for next in get_adjacent_permutations(&curr) {
            let next_hash = hash_permutation(&next);
            if !visited.contains_key(&next_hash) {
                visited.insert(next_hash, visited.get(&curr_hash).unwrap() + 1);
                queue.push_back(next);
            }
            if next_hash == target_hash {
                return Some(*visited.get(&next_hash).unwrap());
            }
        }
    }
    None
}

/// A Python module implemented in Rust.
#[pymodule]
mod rubixpy {
    use pyo3::prelude::*;

    /// Formats the sum of two numbers as string.
    #[pyfunction]
    fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
        Ok((a + b).to_string())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    use test::Bencher;

    #[test]
    fn test_transform() {
        assert_eq!(Permutation::new().t(TS).out(), TS);
    }

    #[test]
    fn test_search() {
        let p = Permutation::new().tn(TR, 2).tn(TT, 2).out();
        let mut hm = HashMap::new();
        hm.insert(hash_permutation(&p), 0);
        let result = search(&mut hm, VecDeque::from([p]), hash_permutation(&BASE));
        assert_eq!(result, Some(4));
    }

    #[test]
    fn test_init_search() {
        let p = Permutation::new()
            .tn(TR, 2)
            .tn(TT, 2)
            .tn(TR, 2)
            .tn(TT, 2)
            .out();
        let result = init_search(p, hash_permutation(&BASE));
        assert_eq!(result, Some(8));
    }

    #[bench]
    fn bench_init_search(b: &mut Bencher) {
        let p = Permutation::new()
            .tn(TR, 2)
            .tn(TT, 2)
            .tn(TR, 2)
            .tn(TT, 2)
            .out();
        b.iter(|| {
            let result = init_search(p, hash_permutation(&BASE));
            assert_eq!(result, Some(8));
        });
    }
}
