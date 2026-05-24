# MiMo Agent Benchmark

MiMo Agent Benchmark is a small benchmark suite for testing Xiaomi MiMo on coding-agent and developer-assistant tasks.

## Problem
Model quality is hard to compare without repeatable tasks. Developers need simple benchmarks for coding, debugging, shell assistance, and documentation workflows.

## Solution
This project runs a fixed set of prompts against MiMo API, measures latency, stores outputs, and produces JSON reports that can be compared over time.

## Core Features
- Coding task prompts
- Linux debugging prompt
- Latency measurement
- JSON output report
- Simple Python runner

## Architecture
1. Load benchmark tasks
2. Send each task to MiMo API
3. Measure latency per request
4. Save output and metadata
5. Compare results manually or in CI

## Example Tasks
- Fix broken Python code
- Generate regex for email extraction
- Explain Linux disk cleanup safely

## Files
- `benchmark.py` — benchmark runner
- `requirements.txt` — Python dependencies

## Roadmap
- Add scoring rules
- Add unit-test based evaluation
- Export Markdown reports
- Compare MiMo vs other models
- GitHub Actions scheduled benchmark

## Why Xiaomi MiMo
This project shows how MiMo performs in real developer-assistant workloads, not only generic chat.

## Project Maturity
- MVP code available
- Architecture documented
- Roadmap documented
- CI configured
- MIT licensed

## Links
- [Architecture](ARCHITECTURE.md)
- [Roadmap](ROADMAP.md)
- [Examples](examples/basic.md)
