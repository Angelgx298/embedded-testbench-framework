#!/bin/bash
echo "[INFO] Cleaning up environment..."
[ -f .socat.pid ] && kill $(cat .socat.pid) && rm .socat.pid
sudo ip link delete vcan0 2>/dev/null
echo "[OK] Environment clean."