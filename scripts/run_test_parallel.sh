#!/usr/bin/env bash

# -------- common thread limits --------
export OMP_NUM_THREADS=3 &&
export MKL_NUM_THREADS=3 &&
export OPENBLAS_NUM_THREADS=3 &&
export NUMEXPR_NUM_THREADS=3 &&

# -------- run A on cores 0–4 --------
taskset -c 6-8 \
python -m pipeline.test_CEM_N