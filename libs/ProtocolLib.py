import serial
import can
import socket
import time

class ProtocolLib:
    def __init__(self):
        self.timeout = 2.0
        self.uart = None

    def _uart_connect(self, port):
        if not self.uart:
            self.uart = serial.Serial(port, 9600, timeout=self.timeout)
            self.uart.reset_input_buffer()

    def uart_send_command(self, port, command):
        self._uart_connect(port)
        self.uart.write(f"{command}\n".encode())
        self.uart.flush()

    def uart_expect_response(self, port, expected_prefix):
        self._uart_connect(port)
        start_time = time.time()
        
        while self.uart.in_waiting == 0:
            if time.time() - start_time > self.timeout:
                raise AssertionError(f"Timeout: No response on {port}")
            time.sleep(0.1)
        
        response = self.uart.readline().decode().strip()
        if expected_prefix not in response:
            raise AssertionError(f"Expected '{expected_prefix}' but got '{response}'")
        return response

    def can_send_telemetry(self, channel, msg_id, data_hex):
        with can.Bus(interface='socketcan', channel=channel) as bus:
            msg = can.Message(
                arbitration_id=int(msg_id, 16),
                data=bytes.fromhex(data_hex),
                is_extended_id=False
            )
            bus.send(msg)

    def udp_send_and_receive(self, ip, port, message):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.settimeout(self.timeout)
            sock.sendto(message.encode(), (ip, int(port)))
            data, _ = sock.recvfrom(1024)
            return data.decode()