import pyshark
import csv

# Update with your correct file paths
pcap_file = r"C:\Users\hp\OneDrive\Desktop\test.pcap"
output_csv = r"C:\Users\hp\OneDrive\Desktop\detailed_flows_output.csv"

cap = pyshark.FileCapture(pcap_file, use_json=True)

# Open CSV for writing
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Source IP', 'Destination IP', 'Protocol',
        'Source Port', 'Destination Port',
        'Packet Length', 'Relative Time'
    ])

    for pkt in cap:
        try:
            src_ip = pkt.ip.src
            dst_ip = pkt.ip.dst
            proto = pkt.transport_layer
            src_port = pkt[pkt.transport_layer].srcport
            dst_port = pkt[pkt.transport_layer].dstport
            pkt_len = int(pkt.length)
            rel_time = float(pkt.sniff_timestamp)

            writer.writerow([
                src_ip, dst_ip, proto,
                src_port, dst_port,
                pkt_len, rel_time
            ])

        except AttributeError:
            # Skip non-IP/non-TCP/UDP packets
            continue

print(" Done! Detailed flow data saved to:", output_csv)
