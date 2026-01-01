test:
    uv run cargo test

build-dev:
    uv run maturin develop

run-dev: build-dev
    uv run python ./rubixpy/main.py

bench:
    uv run cargo bench

bench1:
    uv run cargo run --bin bench1 --no-default-features