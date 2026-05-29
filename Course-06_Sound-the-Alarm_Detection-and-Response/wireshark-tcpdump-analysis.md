# Wireshark and tcpdump Packet Analysis

**Analyst:** [Your Name]  
**Date:** [Date]  
**Tools Used:** Wireshark, tcpdump  
**Capture File:** `sample-capture.pcap` (fictional)

---

## Overview

As part of investigating network-layer security, I captured and analysed network packets using both `tcpdump` (command-line) and Wireshark (GUI). The goal was to identify suspicious traffic patterns and understand how normal versus anomalous network communication appears at the packet level.

---

## Part 1: tcpdump Analysis

### Capturing Traffic

To capture live packets on the network interface and save to a file:

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

To read a saved capture file:

```bash
sudo tcpdump -r capture.pcap -v
```

### Filtering with tcpdump

| Purpose | Command |
|---------|---------|
| Filter by source IP | `tcpdump -r capture.pcap src host 192.168.1.105` |
| Filter by destination port | `tcpdump -r capture.pcap dst port 443` |
| Filter DNS traffic | `tcpdump -r capture.pcap port 53` |
| Show packets as ASCII | `tcpdump -r capture.pcap -A` |
| Limit output to N packets | `tcpdump -r capture.pcap -c 10` |

### Sample tcpdump Output

```
13:24:05.123456 IP 192.168.1.105.54321 > 8.8.8.8.53: A? suspiciousdomain.com. (36)
13:24:05.234567 IP 8.8.8.8.53 > 192.168.1.105.54321: A suspiciousdomain.com. (52)
```

**Observation:** Repeated DNS lookups to an unusual external domain from the same internal host may indicate DNS tunnelling or C2 communication.

---

## Part 2: Wireshark Analysis

### Loading a Capture File

Opened `capture.pcap` in Wireshark using **File → Open**. The packet list displayed all captured frames with timestamps, source/destination IP, protocol, and info.

### Applying Display Filters

| Purpose | Wireshark Filter |
|---------|-----------------|
| Filter by IP address | `ip.addr == 192.168.1.105` |
| Filter by protocol | `dns` or `http` or `tcp` |
| Filter by destination port | `tcp.dstport == 443` |
| Show only failed TCP handshakes | `tcp.flags.syn == 1 && tcp.flags.ack == 0` |

### Observations from Packet Analysis

#### Finding 1: Unencrypted HTTP Traffic

Filtered for `http` traffic and identified cleartext data in packet payloads, including potential credential information.

- **Protocol:** HTTP (port 80)
- **Risk:** Sensitive data transmitted without encryption
- **Recommendation:** Enforce HTTPS across all web communications

#### Finding 2: SYN Flood Indicators

Observed a large volume of TCP SYN packets from a single external IP to multiple internal ports within a short time window.

- **Pattern:** Port scanning / SYN flood behaviour
- **External IP:** 203.0.113.42 (fictitious)
- **Risk:** Potential reconnaissance or DoS attack
- **Recommendation:** Rate-limit inbound connections; block suspicious source IP at the firewall

#### Finding 3: Unusual DNS Query Lengths

DNS queries from `192.168.1.105` had unusually long subdomain labels (40–60 characters), consistent with DNS tunnelling patterns.

- **Protocol:** DNS (UDP port 53)
- **Indicator:** Excessive query length; queries to unregistered domain
- **Risk:** Possible data exfiltration via DNS
- **Recommendation:** Deploy DNS monitoring and filtering; investigate affected host

---

## Summary

| Tool | Key Finding | Risk Level |
|------|-------------|-----------|
| tcpdump | Repeated DNS lookups to suspicious domain | High |
| Wireshark | Unencrypted HTTP with sensitive data | Medium |
| Wireshark | SYN flood pattern from external IP | High |
| Wireshark | DNS tunnelling indicators | High |

Packet analysis is a powerful skill for detecting threats that may bypass higher-level security tools. Both `tcpdump` and Wireshark complement each other — tcpdump for quick command-line capture and filtering, Wireshark for deep visual inspection and protocol dissection.
