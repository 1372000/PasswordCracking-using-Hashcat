# Hashcat Project: Efficient Hash Cracking with GPUs

## Overview

This project demonstrates how to use **Hashcat**, the world's fastest password cracking tool, to recover passwords by utilizing various hash types and attack modes. This project includes an optimized workflow with GPU acceleration and automation through Python scripting. The project is designed to be used for security audits, penetration testing, and password recovery.

## Features
- **GPU Acceleration**: Leverage NVIDIA GPUs to significantly speed up hash cracking.
- **Multiple Hash Algorithms**: Supports MD5, SHA1, and other popular hashing algorithms.
- **Flexible Attack Modes**: Dictionary attacks, brute-force, and rule-based attacks.
- **Automation**: Run Hashcat with multiple configurations using Python scripts.
- **Docker Support**: Easily deploy the environment with Docker for portability.

## Requirements

- **Hashcat**: Pre-installed or available via Docker.
- **NVIDIA GPU** (Optional, but recommended for performance): Ensure CUDA and NVIDIA drivers are installed.
- **Python**: Required for running the Python automation scripts.
- **Docker** (Optional): For isolated environment deployment.

## Setup Instructions
**Install dependencies**
If you're not using Docker, install Hashcat and Python dependencies:

```bash
1.sudo apt install hashcat

```bash
2.pip install -r requirements.txt

**Running Hashcat with Docker**
To run Hashcat using Docker:

```bash
1.docker-compose up

**Running the Python Scripts**
To run the main cracking script:

```bash
1.python3 scripts/run_hashcat.py

**To benchmark your GPU performance:**

```bash
1.python3 scripts/benchmark.py

### 1. Clone the repository

```bash
git clone https://github.com/13072000/hashcat_project.git
cd hashcat_project
