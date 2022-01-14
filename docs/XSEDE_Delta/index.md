Delta User Guide
Last update: January 7, 2022



Status Updates and Notices
Delta is tentatively scheduled to enter production in Q2 2022.

Introduction
Delta is a dedicated, eXtreme Science and Engineering Science Discovery Environment (XSEDE) allocated resource designed by HPE and NCSA, delivering a highly capable GPU-focused compute environment for GPU and CPU workloads.  Besides offering a mix of standard and reduced precision GPU resources, Delta also offers GPU-dense nodes with both NVIDIA and AMD GPUs.  Delta provides high performance node-local SSD scratch filesystems, as well as both standard lustre and relaxed-POSIX parallel filesystems spanning the entire resource.

Delta's standard CPU nodes are each powered by two 64-core AMD EPYC 7763 ("Milan") processors, with 256 GB of DDR4 memory.  The Delta GPU resource has four node types: one with 4 NVIDIA A100 GPUs (40 GB HBM2 RAM each) connected via NVLINK and 1 64-core AMD EPYC 7763 ("Milan") processor, the second with 4 NVIDIA A40 GPUs (48 GB GDDR6 RAM) connected via PCIe 4.0 and 1 64-core AMD EPYC 7763 ("Milan") processor, the third with 8 NVIDIA A100 GPUs in a dual socket AMD EPYC 7763 (128-cores per node) node with 2 TB of DDR4 RAM and NVLINK,  and the fourth with 8 AMD MI100 GPUs (32GB HBM2 RAM each) in a dual socket AMD EPYC 7763 (128-cores per node) node with 2 TB of DDR4 RAM and PCIe 4.0. 

Delta has 124 standard CPU nodes, 100 4-way A100-based GPU nodes, 100 4-way A40-based GPU nodes, 5 8-way A100-based GPU nodes, and 1 8-way MI100-based GPU node.  Every Delta node has high-performance node-local SSD storage (800 GB for CPU nodes, 1.6 TB for GPU nodes), and is connected to the 7 PB Lustre parallel filesystem via the high-speed interconnect.  The Delta resource uses the SLURM workload manager for job scheduling.  

Delta supports the XSEDE core software stack, including remote login, remote computation, data movement, science workflow support, and science gateway support toolkits.





Figure 1. Delta System

Delta is supported by the National Science Foundation under Grant No. OAC-2005572.

Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

Delta is now accepting proposals.
Top of Page

Account Administration
Setting up Your Account
Allocation Information
How to Access the System
ssh, scp, sftp
Globus Online connected to endpoint NCSA#Delta
Open OnDemand 
Configuring Your Account
default shell, changing your shell, changing your password
environment variables
using Modules (or other environment manager)
System Architecture
Delta is designed to help applications transition from CPU-only to GPU or hybrid CPU-GPU codes. Delta has some important architectural features to facilitate new discovery and insight:

a single processor architecture (AMD) across all node types: CPU and GPU
support for NVIDIA A100 MIG GPU partitioning allowing for fractional use of the A100s if your workload isn't able to exploit an entire A100 efficiently
ray tracing hardware support from the NVIDIA A40 GPUs
9 large memory (2 TB) nodes 
a low latency and high bandwidth HPE/Cray Slingshot interconnect between compute nodes
lustre for home, projects and scratch file systems
support for relaxed and non-posix IO
shared-node jobs and the single core and single MIG GPU slice
Resources for persistent services in support of Gateways, Open OnDemand, Data Transport nodes..., 
Unique AMD MI-100 resource  
