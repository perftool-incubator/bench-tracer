# Bench-tracer

## Purpose
Crucible interface for running the Linux kernel osnoise and timerlat workloads/tracers. Requires cpu-partitioning to define WORKLOAD_CPUS and HK_CPUS.

## Language
- Bash for client execution scripts
- Python for post-processing (`tracer-post-process.py`)

## Key Files
| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: client scripts, parameter transformations |
| `multiplex.json` | Parameter validation rules, unit conversions, and presets for multiplex |
| `benchmark-metadata.json` | Machine-readable description and output file list (consumed by `crucible benchmarks list`) |
| `tracer-base` | Base setup shared by other scripts |
| `tracer-client` | Client-side execution: configures and runs osnoise/timerlat tracers |
| `tracer-runtime` | Runtime extraction |
| `tracer-post-process.py` | Post-processing script |
| `workshop.json` | Engine image build requirements |

## Configuration
- `--tracer <osnoise|timerlat>` — Tracer to use (default: osnoise)
- `--duration <seconds>` — Collection duration (default: 60)
- `--period`, `--runtime` — Tracer timing parameters
- `--stack`, `--cpu`, `--events` — Tracing options

## Conventions
- Primary branch is `main`
- Requires cpu-partitioning for WORKLOAD_CPUS/HK_CPUS environment variables
- Standard Bash modelines and 4-space indentation
- Python code follows 4-space indentation with standard modelines
