# Embedded System Testbench Framework

[![CI](https://github.com/Angelgx298/embedded-testbench-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/Angelgx298/embedded-testbench-framework/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A professional automated verification framework for embedded systems. It features a multi-threaded device emulator supporting UART, CAN, and UDP protocols, coupled with a robust Robot Framework test suite.

## Key Features

- **Asynchronous Target Emulator**: Python-based multi-threaded engine simulating real-time hardware behavior.
- **Protocol Abstraction Layer**: High-level library (`ProtocolLib`) for seamless interaction with UART, CAN, and UDP interfaces.
- **Robust Testing Logic**: Advanced Robot Framework keywords implemented with retry mechanisms to handle asynchronous bus latencies and race conditions.
- **Industrial-Grade CI/CD**: Fully automated pipeline using GitHub Actions for code quality (Ruff) and syntax validation.

## Project Architecture

- `src/target_emulator.py`: The Device Under Test (DUT) logic, managing concurrent bus interfaces.
- `libs/ProtocolLib.py`: Specialized driver for low-level protocol communication.
- `tests/connectivity.robot`: System-level integration test suite.
- `scripts/setup_env.sh`: Infrastructure automation for virtual networking (vcan, socat).

## Installation & Usage

### 1. Prerequisites

Ensure you are running a Linux environment (for `vcan` and `socat` support) and install the dependencies:

```bash
pip install -r requirements.txt
```

### 2. Environment Setup

Initialize virtual CAN and UART bridge interfaces:

```bash
chmod +x scripts/setup_env.sh
./scripts/setup_env.sh
```

### 3. Execution

In separate terminals, follow this sequence:

1. **Run the Emulator**:

   ```bash
   python src/target_emulator.py
   ```

2. **Launch the Test Suite**:
   ```bash
   robot tests/connectivity.robot
   ```

### 4. CI/CD Integration

This repository uses **GitHub Actions** to enforce high engineering standards on every push:

- **Linting & Formatting**: Powered by `Ruff` to ensure PEP8 compliance and clean code.
- **Syntax Validation**: Automatic verification of Robot Framework libraries and test suites to prevent broken builds.

## Technical Notes: Solving Race Conditions

A core challenge in asynchronous embedded testing is bus latency. This framework avoids flaky tests by implementing a **smart retry mechanism** using Robot Framework's `Wait Until Keyword Succeeds`.

Instead of using fixed `Sleep` commands—which make tests slow and unreliable—the suite polls the system state with a defined timeout. This ensures the tests are as fast as the hardware allows while remaining deterministic.

---

Developed by [Angelgx298](https://github.com/Angelgx298)
