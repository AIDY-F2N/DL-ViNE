# DL-ViNE : Reinforcement Learning Algorithm for Efficient Virtual Network Embedding under Direct Link Constraints

![Lab Logo](logo_aidy_f2n.png)

## Description

The rise of 5G and upcoming 6G technologies has introduced a broad spectrum of industrial and service applications with diverse Quality of Service (QoS) and resource requirements. Network Slicing has emerged as a critical paradigm to meet these demands by creating multiple logical Virtual Networks (VNs), or "slices," on shared physical infrastructures. This process, referred to as the Virtual Network Embedding (VNE) problem, involves optimally allocating resources to maximize utilization and operator benefits.

With Kubernetes becoming the leading container orchestration platform, most modern infrastructures are now hosted on Kubernetes clusters. Kubernetes enforces direct communication between pods, which necessitates a direct-link mapping approach in the VNE process. However, existing VNE solutions predominantly rely on path-based mappings and shortest-path algorithms, leaving the direct-link scenario unexplored.

DL-ViNE (Direct Link Virtual Network Embedding) addresses this gap with a novel reinforcement learning-based algorithm tailored to the direct-link constraints of Kubernetes-hosted infrastructures. By leveraging slice specifications and intelligent node selection, DL-ViNE enhances slice acceptance rates, improves resource utilization, and optimizes runtime performance.


## Prerequisites

To use DL-ViNE, you need the following installed:

1. **Julia** (version 1.6+ recommended)
   - [Download Julia](https://julialang.org/downloads/)
   - Install Julia packages (instructions below).

2. **Python 3.8+** (for instance generation and plot visualization)
   - Required Python packages:
     - `random`
     - `os`
     - `networkx`
     - `json`
     - `matplotlib`



## Installation Instructions

### 1. Clone the Repository
Start by cloning this repository:
```bash
git clone https://github.com/AIDY-F2N/DL-ViNE.git
cd DL-ViNE




## Keywords
**5G**, **Network Slicing**, **Virtual Network Embedding (VNE)**, **Reinforcement Learning (RL)**, **Kubernetes**