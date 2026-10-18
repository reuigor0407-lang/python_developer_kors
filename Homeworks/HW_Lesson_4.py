# Блок 1: Рядки (str) — Валідація та нормалізація
import array

control_command = "cOnNeCt:192.168.1.1:8080\n"
control_command = control_command.strip().split(":")

command = control_command[0].lower()
ip_address = control_command[1]
port = control_command[2]

# Блок 2: Байти (bytes) — Серіалізація для мережі

ip_bytes = ip_address.encode("ascii")
# ip_bytes[0] = 2
# print(ip_bytes)

# Виникло виключення:
#   'TypeError: 'bytes' object does not support item assignment'
# Тому що bytes - це не змінний тип даних

# Блок 3: Масиви байтів (bytearray) — Модифікація пакета на льоту

packet = bytearray(5)

packet[0] = 0xAA
packet[-1] = 0xFF

packet.extend(ip_bytes)
print(len(packet))

# Блок 4: Списки (list) — Черга відправки даних

packet_queue = []

packet_queue.extend([command, ip_bytes, packet])
packet_queue.insert(0, "PING")

processed_packet = packet_queue.pop()

# Блок 5: Кортежі (tuple) — Незмінний архів (Лог)

log_entry = (tuple(packet_queue), processed_packet)

# log_entry не можна використовувати як ключ dict, тому що processed_packet
# має тип bytearray, а він є змінним та нехешованим типом даних.

# Блок 6: Типізовані масиви (array.array) — Економія пам'яті

import array

ports = array.array("H")
ports.extend([80, 443, int(port)])

# ports.append("8080")
# При спробі додати до масиву рядок, виникає помилка:
#   'TypeError: 'str' object cannot be interpreted as an integer'

# Блок 7: Іменовані кортежі (collections.namedtuple) — Читабельність коду

from collections import namedtuple

Session = namedtuple("Session", ["command", "ip", "port", "status"])

session = Session(command, ip_address, int(port), "Active")

print(session.ip)
print(session.status)


