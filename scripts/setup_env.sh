#!/bin/bash

# Setup Virtual CAN interface
echo "[INFO] Configuring Virtual CAN interface..."
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan 2>/dev/null || echo "[INFO] vcan0 already exists"
sudo ip link set up vcan0

# Create UART bridge: /tmp/ttyV0 (Test Suite) <-> /tmp/ttyV1 (Simulator)
echo "[INFO] Creating virtual UART bridge..."
socat -d -d PTY,link=/tmp/ttyV0,raw,echo=0 PTY,link=/tmp/ttyV1,raw,echo=0 &
SOCAT_PID=$!

echo "------------------------------------------------"
echo "SIMULATION ENVIRONMENT ACTIVE:"
echo " - CAN: vcan0"
echo " - UART: /tmp/ttyV0 (Test) | /tmp/ttyV1 (Sim)"
echo " - Ethernet: Localhost (UDP)"
echo "------------------------------------------------"

# Save PID for cleanup
echo $SOCAT_PID > .socat.pid
echo "[INFO] To terminate the environment, run: kill \$(cat .socat.pid)"