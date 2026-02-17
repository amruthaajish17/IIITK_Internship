# IIITK_Internship
Behavioural Fingerprinting for Insider Threat Detection: An unsupervised machine learning project developed during my internship at IIIT Kottayam to detect anomalous network patterns using Isolation Forest, DBSCAN, and KMeans clustering.

# Behavioural Fingerprinting for Insider Threat Detection 🛡️🔍

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 📌 Project Overview
This repository contains the source code and documentation for my research internship project aimed at detecting **Insider Threats**—security risks originating from within an organization. Unlike external attacks, insider threats are difficult to detect using traditional signatures because they involve legitimate access.

This project utilizes **Behavioural Fingerprinting** to profile normal network traffic patterns and identifies deviations using **Unsupervised Machine Learning** techniques.

> **Internship Context:** > **Institute:** Indian Institute of Information Technology Kottayam (IIITK)  
> **Guide:** Dr. Fasila K A  
> **Duration:** May 2025 – June 2025

## 🚀 Key Features
* **Traffic Parsing:** Converts raw `.pcap` network traffic files into structured CSV datasets using `pyshark`.
* **Feature Extraction:** Analyzes flow-level features such as Packet Length, Relative Time, Source/Destination IPs, and Ports.
* **Anomaly Detection:** Implements **Isolation Forest** to flag statistical outliers in network behavior.
* **Clustering Analysis:** Uses **KMeans** and **DBSCAN** to group similar traffic flows and visualize normal vs. abnormal clusters.
* **Visualization:** Generates scatter plots to visually represent clusters and potential threats.

## 🛠️ Tech Stack
* **Language:** Python
* **Packet Processing:** Wireshark, Pyshark
* **Machine Learning:** Scikit-learn (Isolation Forest, KMeans, DBSCAN)
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn

## 📂 Repository Structure
```text
├── csvtopic.py                 # Main script for ML modeling and visualization
├── pcap_to_csv.py              # Script to parse .pcap files into CSV format
├── detailed_flows_output.csv   # Processed dataset representing network flows
├── Report.docx                 # Detailed internship report
├── Presentation.pptx           # Project presentation slides
└── output/                     # Generated plots (KMeans, DBSCAN, Isolation Forest)
