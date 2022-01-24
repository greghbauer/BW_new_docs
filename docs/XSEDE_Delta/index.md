# **Delta User Guide**

*Last update: January 7, 2022*

  

# **Status Updates and Notices**

*Delta* is tentatively scheduled to enter production in Q2 2022.

# **Introduction**

*Delta* is a dedicated, [eXtreme Science and Engineering Science
Discovery Environment (XSEDE)](http://www.xsede.org) allocated resource
designed by HPE and NCSA, delivering a highly capable GPU-focused
compute environment for GPU and CPU workloads.  Besides offering a mix
of standard and reduced precision GPU resources, *Delta* also offers
GPU-dense nodes with both NVIDIA and AMD GPUs.  *Delta* provides high
performance node-local SSD scratch filesystems, as well as both standard
lustre and relaxed-POSIX parallel filesystems spanning the entire
resource.

*Delta's* standard CPU nodes are each powered by two 64-core AMD EPYC
7763 ("Milan") processors, with 256 GB of DDR4 memory.  The *Delta* GPU
resource has four node types: one with 4 NVIDIA A100 GPUs (40 GB HBM2
RAM each) connected via NVLINK and 1 64-core AMD EPYC 7763 ("Milan")
processor, the second with 4 NVIDIA A40 GPUs (48 GB GDDR6 RAM) connected
via PCIe 4.0 and 1 64-core AMD EPYC 7763 ("Milan") processor, the third
with 8 NVIDIA A100 GPUs in a dual socket AMD EPYC 7763 (128-cores per
node) node with 2 TB of DDR4 RAM and NVLINK,  and the fourth with 8 AMD
MI100 GPUs (32GB HBM2 RAM each) in a dual socket AMD EPYC 7763
(128-cores per node) node with 2 TB of DDR4 RAM and PCIe 4.0. 

*Delta* has 124 standard CPU nodes, 100 4-way A100-based GPU nodes, 100
4-way A40-based GPU nodes, 5 8-way A100-based GPU nodes, and 1 8-way
MI100-based GPU node.  Every *Delta* node has high-performance
node-local SSD storage (800 GB for CPU nodes, 1.6 TB for GPU nodes), and
is connected to the 7 PB Lustre parallel filesystem via the high-speed
interconnect.  The *Delta* resource uses the SLURM workload manager for
job scheduling.  

Delta supports the [XSEDE core software
stack](https://www.xsede.org/software), including remote login, remote
computation, data movement, science workflow support, and science
gateway support toolkits.

<img src="./NCSA_Delta_image.png" alt="Colorful triangle" width="400"/>

**Figure 1. Delta System**

Delta is supported by the National Science Foundation under Grant No.
OAC-<span style="color: rgb(0,0,0);">2005572</span>.

Any opinions, findings, and conclusions or recommendations expressed in
this material are those of the author(s) and do not necessarily reflect
the views of the National Science Foundation.

<table class="wrapped">
<tbody>
<tr class="header">
<th style="text-align: center;" class="highlight-yellow"
data-highlight-colour="yellow"><em>Delta</em> is now accepting
proposals.</th>
</tr>

</tbody>
</table>

Top of Page

# **Account Administration**

-   Setting up Your Account
-   Allocation Information
-   How to Access the System
    -   ssh, scp, sftp
    -   Globus Online connected to endpoint NCSA#Delta
    -   Open OnDemand 

## **Configuring Your Account**

-   default shell, changing your shell, changing your password
-   environment variables
-   using Modules (or other environment manager)

# **System Architecture**

<span style="color: rgb(0,0,0);">Delta is designed to help applications
transition from CPU-only to GPU or hybrid CPU-GPU codes. Delta has some
important architectural features to facilitate new discovery and
insight:</span>

-   <span style="color: rgb(0,0,0);">a single processor architecture
    (AMD) across all node types: CPU and GPU</span>
-   <span style="color: rgb(17,17,17);">support for NVIDIA A100 MIG GPU
    partitioning allowing for fractional use of the A100s if your
    workload isn't able to exploit an entire A100 efficiently</span>
-   <span style="color: rgb(0,0,0);">ray tracing hardware support from
    the NVIDIA A40 GPUs</span>
-   <span style="color: rgb(0,0,0);">9 large memory (2 TB) nodes </span>
-   <span style="color: rgb(0,0,0);">a low latency and high bandwidth
    HPE/Cray Slingshot interconnect between compute nodes</span>
-   <span style="color: rgb(0,0,0);">lustre for home, projects and
    scratch file systems</span>
-   <span style="color: rgb(17,17,17);">support for relaxed and
    non-posix IO</span>
-   <span style="color: rgb(17,17,17);">shared-node jobs and the single
    core and single MIG GPU slice</span>
-   <span style="color: rgb(17,17,17);">Resources for persistent
    services in support of Gateways, Open OnDemand, Data Transport
    nodes..., </span>
-   <span style="color: rgb(0,0,0);">Unique AMD MI-100 resource</span>  

## **Model Compute Nodes**

<span style="color: rgb(0,0,0);">The Delta compute ecosystem is composed
of 5 node types: dual-socket CPU-only compute nodes, single socket 4-way
NVIDIA A100 GPU compute nodes, single socket 4-way NVIDIA A40 GPU
compute nodes, dual-socket 8-way NVIDIA A100 GPU compute nodes, and a
single socket 8-way AMD MI100 GPU compute nodes. The CPU-only and 4-way
GPU nodes have 256 GB of RAM per node while the 8-way GPU nodes have 2
TB of RAM. The CPU-only node has 0.8 TB of local storage while all GPU
nodes have 1.6 TB of local storage.</span>

### Table. CPU Compute Node Specifications

<table class="wrapped">
<tbody>
<tr class="header">
<th>Specification</th>
<th>Value</th>
</tr>

<tr class="odd">
<td><p><span>Number of nodes</span></p></td>
<td><p><span>124</span></p></td>
</tr>
<tr class="even">
<td><span>CPU</span></td>
<td><span>AMD Milan (PCIe Gen4)</span></td>
</tr>
<tr class="odd">
<td>Sockets per node</td>
<td>2</td>
</tr>
<tr class="even">
<td><p><span>Cores per socket</span></p></td>
<td><p><span>64</span></p></td>
</tr>
<tr class="odd">
<td>Cores per node</td>
<td>128</td>
</tr>
<tr class="even">
<td><p><span>Hardware threads per core</span></p></td>
<td>1</td>
</tr>
<tr class="odd">
<td><p><span>Hardware threads per node</span></p></td>
<td><p><span>128</span></p></td>
</tr>
<tr class="even">
<td><p><span>Clock rate (GHz)</span></p></td>
<td><p><span>~ 2.45</span></p></td>
</tr>
<tr class="odd">
<td><p><span>RAM (GB)</span></p></td>
<td><p><span>256</span></p></td>
</tr>
<tr class="even">
<td><p><span>Cache (MB) L1/L2/L3</span></p></td>
<td><p><span> 2/32/256</span></p></td>
</tr>
<tr class="odd">
<td><p><span>Local storage (TB)</span></p></td>
<td><p><span>0.8 TB</span></p></td>
</tr>
</tbody>
</table>

### Table. 4-way NVIDIA A40 GPU Compute Node Specifications 

<table class="wrapped">
<tbody>
<tr class="header">
<th>Specification</th>
<th>Value</th>
</tr>

<tr class="odd">
<td>Number of nodes</td>
<td>100</td>
</tr>
<tr class="even">
<td>GPU</td>
<td>NVIDIA A40 
<p><span>(<a
href="https://www.nvidia.com/en-us/data-center/a40/#specs">Vendor
page</a>)</span></p></td>
</tr>
<tr class="odd">
<td>GPUs per node</td>
<td>4</td>
</tr>
<tr class="even">
<td>GPU Memory (GB)</td>
<td>48 DDR6 with ECC</td>
</tr>
<tr class="odd">
<td>CPU</td>
<td>AMD Milan</td>
</tr>
<tr class="even">
<td>CPU sockets per node</td>
<td>1</td>
</tr>
<tr class="odd">
<td><p><span>Cores per socket</span></p></td>
<td><p>64</p></td>
</tr>
<tr class="even">
<td>Cores per node</td>
<td>64</td>
</tr>
<tr class="odd">
<td><p><span>Hardware threads per core</span></p></td>
<td>1</td>
</tr>
<tr class="even">
<td><p><span>Hardware threads per node</span></p></td>
<td><p>64</p></td>
</tr>
<tr class="odd">
<td><p><span>Clock rate (GHz)</span></p></td>
<td><p><span>~ 2.45</span></p></td>
</tr>
<tr class="even">
<td><p><span>RAM (GB)</span></p></td>
<td><p><span>256</span></p></td>
</tr>
<tr class="odd">
<td><p><span>Cache (MB) L1/L2/L3</span></p></td>
<td><p><span> 2/32/256</span></p></td>
</tr>
<tr class="even">
<td><p><span>Local storage (TB)</span></p></td>
<td><p><span>1.6 TB</span></p></td>
</tr>
</tbody>
</table>

### Table. 4-way NVIDIA A100 GPU Compute Node Specifications 

<table class="wrapped">
<tbody>
<tr class="header">
<th>Specification</th>
<th>Value</th>
</tr>

<tr class="odd">
<td>Number of nodes</td>
<td>100</td>
</tr>
<tr class="even">
<td>GPU</td>
<td>NVIDIA A100
<p>(<a
href="https://www.nvidia.com/en-us/data-center/a100/#specifications">Vendor
page</a>)</p></td>
</tr>
<tr class="odd">
<td>GPUs per node</td>
<td>4</td>
</tr>
<tr class="even">
<td>GPU Memory (GB)</td>
<td>40 </td>
</tr>
<tr class="odd">
<td>CPU</td>
<td>AMD Milan</td>
</tr>
<tr class="even">
<td>CPU sockets per node</td>
<td>2</td>
</tr>
<tr class="odd">
<td><p><span>Cores per socket</span></p></td>
<td><p>64</p></td>
</tr>
<tr class="even">
<td>Cores per node</td>
<td>128</td>
</tr>
<tr class="odd">
<td><p><span>Hardware threads per core</span></p></td>
<td>1</td>
</tr>
<tr class="even">
<td><p><span>Hardware threads per node</span></p></td>
<td>128</td>
</tr>
<tr class="odd">
<td><p><span>Clock rate (GHz)</span></p></td>
<td><p><span>~ 2.45</span></p></td>
</tr>
<tr class="even">
<td><p><span>RAM (GB)</span></p></td>
<td><p><span>256</span></p></td>
</tr>
<tr class="odd">
<td><p><span>Cache (MB) L1/L2/L3</span></p></td>
<td><p><span> 2/32/256</span></p></td>
</tr>
<tr class="even">
<td><p><span>Local storage (TB)</span></p></td>
<td><p><span>1.6 TB</span></p></td>
</tr>
</tbody>
</table>

### Table. 8-way NVIDIA A100 GPU Large Memory  Compute Node Specifications 

<table class="wrapped">
<tbody>
<tr class="header">
<th>Specification</th>
<th>Value</th>
</tr>

<tr class="odd">
<td>Number of nodes</td>
<td>5</td>
</tr>
<tr class="even">
<td>GPU</td>
<td>NVIDIA A100
<p>(<a
href="https://www.nvidia.com/en-us/data-center/a100/#specifications">Vendor
page</a>)</p></td>
</tr>
<tr class="odd">
<td>GPUs per node</td>
<td>8</td>
</tr>
<tr class="even">
<td>GPU Memory (GB)</td>
<td>40 </td>
</tr>
<tr class="odd">
<td>CPU</td>
<td>AMD Milan</td>
</tr>
<tr class="even">
<td>CPU sockets per node</td>
<td>2</td>
</tr>
<tr class="odd">
<td><p><span>Cores per socket</span></p></td>
<td><p>64</p></td>
</tr>
<tr class="even">
<td>Cores per node</td>
<td>128</td>
</tr>
<tr class="odd">
<td><p><span>Hardware threads per core</span></p></td>
<td>1</td>
</tr>
<tr class="even">
<td><p><span>Hardware threads per node</span></p></td>
<td><p>128</p></td>
</tr>
<tr class="odd">
<td><p><span>Clock rate (GHz)</span></p></td>
<td><p><span>~ 2.45</span></p></td>
</tr>
<tr class="even">
<td><p><span>RAM (GB)</span></p></td>
<td><p><span>2,048</span></p></td>
</tr>
<tr class="odd">
<td><p><span>Cache (MB) L1/L2/L3</span></p></td>
<td><p><span> 2/32/256</span></p></td>
</tr>
<tr class="even">
<td><p><span>Local storage (TB)</span></p></td>
<td><p><span>1.6 TB</span></p></td>
</tr>
</tbody>
</table>

### Table. 8-way AMD MI100 GPU Large Memory Compute Node Specifications 

<table class="wrapped">
<tbody>
<tr class="header">
<th>Specification</th>
<th>Value</th>
</tr>

<tr class="odd">
<td>Number of nodes</td>
<td>1</td>
</tr>
<tr class="even">
<td>GPU</td>
<td>AMD MI100  
<p><span>(<a
href="https://www.amd.com/en/products/server-accelerators/instinct-mi100">Vendor
page</a>)</span></p></td>
</tr>
<tr class="odd">
<td>GPUs per node</td>
<td>8</td>
</tr>
<tr class="even">
<td>GPU Memory (GB)</td>
<td>32</td>
</tr>
<tr class="odd">
<td>CPU</td>
<td>AMD Milan</td>
</tr>
<tr class="even">
<td>CPU sockets per node</td>
<td>2</td>
</tr>
<tr class="odd">
<td><p><span>Cores per socket</span></p></td>
<td><p>64</p></td>
</tr>
<tr class="even">
<td>Cores per node</td>
<td>128</td>
</tr>
<tr class="odd">
<td><p><span>Hardware threads per core</span></p></td>
<td>1</td>
</tr>
<tr class="even">
<td><p><span>Hardware threads per node</span></p></td>
<td><p>128</p></td>
</tr>
<tr class="odd">
<td><p><span>Clock rate (GHz)</span></p></td>
<td><p><span>~ 2.45</span></p></td>
</tr>
<tr class="even">
<td><p><span>RAM (GB)</span></p></td>
<td><p><span>2,048</span></p></td>
</tr>
<tr class="odd">
<td><p><span>Cache (MB) L1/L2/L3</span></p></td>
<td><p><span> 2/32/256</span></p></td>
</tr>
<tr class="even">
<td><p><span>Local storage (TB)</span></p></td>
<td><p><span>1.6 TB</span></p></td>
</tr>
</tbody>
</table>

## **Login Nodes**

Describe login node/s.

## **Specialized Nodes**

Delta will support data transfer nodes or nodes in support of other
services.

## **Network**

Delta will be connected to the NPCF core router & exit infrastructure
via two 100Gbps connections, NCSA's 400Gbps+ of WAN connectivity will
carry traffic to/from users on an optimal peering. 

Delta resources will be inter-connected with HPE/Cray's 100Gbps/200Gbps
SlingShot interconnect.  

## **File Systems**

Note:  Users of Delta have access to 3 file systems at the time of
system launch, a fourth relaxed-POSIX file system will be made available
at a later date. 

### **Delta**  
The *Delta* storage infrastructure provides users with their $HOME and
$SCRATCH areas.  These file systems are mounted across all Delta systems
and are accessible on the Delta DTN Endpoints.  The aggregate
performance of this subsystem is 70GB/s and it has 6PB of usable space.
 These file systems run Lustre via DDN's ExaScaler 6 stack (Lustre 2.14
based)

<u>Hardware:  
</u>DDN SFA7990XE (Quantity: 3), each unit contains

-   One additional SS9012 enclosure
-   168 x 16TB SAS Drives
-   7 x 1.92TB SAS SSDs

<u>Future Hardware:  
</u>An additional pool of NVME flash from DDN will be installed in early
Spring 2022.  This flash will initially be deployed as a tier for "hot"
data in scratch.  This subsystem will have an aggregate performance of
600GB/s and will have 3PB of capacity. As noted above this subsystem
will transition to a relax POSIX namespace file system, communications
on that timeline will be announced as updates are available.  

### **Taiga**
*Taiga* is NCSA’s global file system which provides users with their
$WORK area.  This file system is mounted across all Delta systems at
/taiga (also /taiga/nsf/delta is bind mounted at /projects) and is
accessible on both the *Delta* and *Taiga* DTN endpoints.  For NCSA &
Illinois researchers, *Taiga* is also mounted on *HAL* and *Radiant*. 
This storage subsystem has an aggregate performance of 140GB/s and 1PB
of its capacity allocated to users of the *Delta* system. /taiga is a
Lustre file system running DDN Exascaler.  

<u>Hardware:  
</u>DDN SFA400NVXE (Quantity: 2), each unit contains

-   4 x SS9012 enclosures
-   NVME for metadata and small files

DDN SFA18XE (Quantity: 1), each unit contains

-   10 x SS9012 enclosures

  

<table class="wrapped">
<tbody>
<tr class="odd">
<td><p><strong>File System</strong></p></td>
<td><p><strong>Quota</strong></p></td>
<td><strong>Snapshots</strong></td>
<td><strong>Purged</strong></td>
<td><p><strong>Key Features</strong></p></td>
</tr>
<tr class="even">
<td><p><span>$HOME</span></p></td>
<td><strong>25GB. </strong>400,000 files per user.</td>
<td>No/TBA</td>
<td>No</td>
<td>Area for software, scripts, job files, etc. <strong>NOT</strong>
intended as a source/destination for I/O during jobs</td>
</tr>
<tr class="odd">
<td><p><span>$WORK</span></p></td>
<td><strong>500 GB</strong>. Up to 1-25 TB  by allocation request</td>
<td>No/TBA</td>
<td>No</td>
<td>Area for shared data for a project, common data sets, software,
results, etc.</td>
</tr>
<tr class="even">
<td><p><span>$SCRATCH</span></p></td>
<td><strong>1000 GB</strong>. Up to 1-100 TB by allocation request.</td>
<td>No</td>
<td>Yes; files older than 30-days (access time)</td>
<td>Area for computation, largest allocations, where I/O from jobs
should occur</td>
</tr>
</tbody>
</table>

**Top of Page**

# **Accessing the System**

Describe access to the system

-   NCSA Duo enabled multi-factor authentication
To ssh to Delta using your local NCSA username: `ssh username@login.delta.ncsa.illinois.edu`

-   available via SSO hub

List and detail methods (e.g., ssh, Globus, gsissh), providing
command-line examples.

## **XSEDE Single Sign-On Hub**

[XSEDE](http://www.xsede.org) users can also access Delta via the [XSEDE
Single Sign-On Hub](https://portal.xsede.org/single-sign-on-hub).

When reporting a problem to the help desk, please execute the gsissh
command with the “-vvv” option and include the verbose output in your
problem description.

# **Citizenship**

**You share Delta with thousands of other users**, and what you do on
the system affects others. Exercise good citizenship to ensure that your
activity does not adversely impact the system and the research community
with whom you share it. Here are some rules of thumb.

List any Best Practices or conversely, a list of don’t’s. Some examples:

-   Don’t run jobs on the login nodes
-   Don’t stress filesystem with known-harmful access patterns (many
    thousands of small files in a single directory)
-   submit an informative help-desk ticket

# **Managing and Transferring Files**

## **File Systems**

-   Tips on navigating any shared file systems
-   Detail any pertinent environment variables, e.g., $HOME, $WORK, and
    any built-in aliases.
-   Tips on backups/storage

## **Transferring your Files**

Discuss methods of transferring files and provide command-line examples

-   scp
-   rsync
-   Globus

## **Sharing Files with Collaborators**

# **Building Software**

  

GCC, AOCC, PGI

OpenMPI ...

OpenMP

OpenACC 

Describe how to build software:

#### **Serial**

To build (compile and link) a serial program in Fortran, C, and C++:

<table class="wrapped" style="text-align: left;">
<tbody>
<tr class="header">
<th style="text-align: center;">GCC</th>
<th style="text-align: center;">AOCC</th>
<th style="text-align: center;">PGI</th>
</tr>

<tr class="odd">
<td
style="text-align: center;"><span>gfortran <em>myprog</em>.f</span><br />
<span>gcc <em>myprog</em>.c</span><br />
<span>g++ <em>myprog</em>.cc</span></td>
<td
style="text-align: center;"><span>flang <em>myprog</em>.f</span><br />
<span>clang <em>myprog</em>.c</span><br />
<span>clang <em>myprog</em>.cc</span></td>
<td
style="text-align: center;"><span>pgfortran <em>myprog</em>.f</span><br />
<span>pgcc <em>myprog</em>.c</span><br />
<span>pgc++ <em>myprog</em>.cc</span></td>
</tr>
</tbody>
</table>

  

#### **MPI**

To build (compile and link) a MPI program in Fortran, C, and C++:

<table class="wrapped" style="text-align: left;">
<tbody>
<tr class="header">
<th style="text-align: center;">MPI Implementation</th>
<th style="text-align: center;">modulefile for MPI/Compiler</th>
<th style="text-align: center;">Build Commands</th>
</tr>

<tr class="odd">
<td style="text-align: center;"><p><br />
</p>
<p>OpenMPI<br />
(<a href="http://www.open-mpi.org/" style="text-decoration: none;">Home
Page</a><span> </span>/<span> </span><a
href="http://www.open-mpi.org/doc/"
style="text-decoration: none;">Documentation</a>)</p></td>
<td style="text-align: center;"><p><br />
</p>
<p><br />
</p>
<p>TBD</p></td>
<td style="text-align: center;" rowspan="2"><p><br />
</p>
<table class="wrapped">
<tbody>
<tr class="odd">
<td style="text-align: right;">Fortran 77:</td>
<td><span>mpif77 <em>myprog</em>.f</span></td>
</tr>
<tr class="even">
<td style="text-align: right;">Fortran 90:</td>
<td><span>mpif90 <em>myprog</em>.f90</span></td>
</tr>
<tr class="odd">
<td style="text-align: right;">C:</td>
<td><span>mpicc <em>myprog</em>.c</span></td>
</tr>
<tr class="even">
<td style="text-align: right;">C++:</td>
<td><span>mpicxx <em>myprog</em>.cc</span></td>
</tr>
</tbody>
</table>
<p><br />
</p></td>
</tr>
<tr class="even">
<td style="text-align: center;">TBD</td>
<td style="text-align: center;">TBD</td>
</tr>
</tbody>
</table>

  

#### **OpenMP**

To build an OpenMP program, use the -fopenmp / -mp option:

<table class="wrapped" style="text-align: left;">
<tbody>
<tr class="header">
<th style="text-align: center;">GCC</th>
<th style="text-align: center;">AOCC</th>
<th style="text-align: center;">PGI</th>
</tr>

<tr class="odd">
<td style="text-align: center;"><span>gfortran
-fopenmp <em>myprog</em>.f</span><br />
<span>gcc -fopenmp <em>myprog</em>.c</span><br />
<span>g++ -fopenmp <em>myprog</em>.cc</span></td>
<td
style="text-align: center;"><span>flang -fopenmp <em>myprog</em>.f</span><br />
<span>clang -fopenmp <em>myprog</em>.c</span><br />
<span>clang -fopenmp <em>myprog</em>.cc</span></td>
<td style="text-align: center;"><span>pgfortran
-mp <em>myprog</em>.f</span><br />
<span>pgcc -mp <em>myprog</em>.c</span><br />
<span>pgc++ -mp <em>myprog</em>.cc</span></td>
</tr>
</tbody>
</table>

#### **Hybrid MPI/OpenMP**

To build an MPI/OpenMP hybrid program, use the -fopenmp / -mp option
with the MPI compiling commands:

<table class="wrapped" style="text-align: left;">
<tbody>
<tr class="header">
<th style="text-align: center;">GCC</th>
<th style="text-align: center;"><br />
</th>
<th style="text-align: center;">PGI</th>
</tr>

<tr class="odd">
<td style="text-align: center;"><span>mpif77
-fopenmp <em>myprog</em>.f</span><br />
<span>mpif90 -fopenmp <em>myprog</em>.f90<br />
mpicc -fopenmp <em>myprog</em>.c</span><br />
<span>mpicxx -fopenmp <em>myprog</em>.cc</span></td>
<td style="text-align: center;"><br />
</td>
<td style="text-align: center;"><span>mpif77
-mp <em>myprog</em>.f</span><br />
<span>mpif90 -mp <em>myprog</em>.f90<br />
mpicc -mp <em>myprog</em>.c</span><br />
<span>mpicxx -mp <em>myprog</em>.cc</span></td>
</tr>
</tbody>
</table>

#### **OpenACC**

To build an OpenACC program, use the -acc option and the -mp option for
multi-threaded:

<table class="wrapped" style="text-align: left;">
<tbody>
<tr class="header">
<th style="text-align: center;">NON-MULTITHREADED</th>
<th style="text-align: center;"><br />
</th>
<th style="text-align: center;">MULTITHREADED</th>
</tr>

<tr class="odd">
<td style="text-align: center;"><span>pgfortran
-acc <em>myprog</em>.f</span><br />
<span>pgcc -acc <em>myprog</em>.c</span><br />
<span>pgc++ -acc <em>myprog</em>.cc</span></td>
<td style="text-align: center;"><br />
</td>
<td style="text-align: center;"><span>pgfortran -acc
-mp <em>myprog</em>.f</span><br />
<span>pgcc -acc -mp <em>myprog</em>.c</span><br />
<span>pgc++ -acc -mp <em>myprog</em>.cc</span></td>
</tr>
</tbody>
</table>

  

-   list compilers and recommendations
-   any architecture-specific flags
-   how to build 3rd party software in your account

# **Software**

-   lmod
-   spack/EasyBuild
-   NVIDIA NGC containers
-   OpenCL
-   CUDA

  

-   URL to XSEDE software inventory 

Please open a service request ticket by sending email to
<help@ncsa.illinois.edu> for help with software not currently installed
on the Delta system. For single user or single project use cases the
preference is for the user to use the spack software package manager to
install software locally against the system spack installation as
documented &lt;here&gt;. Delta support staff are available to provide
limited assistance. For general installation requests the Delta project
office will review each requests for broad use and installation effort.

# **Launching Applications (TBD)**

-   Launching One Serial Application
-   Launching One Multi-Threaded Application
-   Launching One MPI Application
-   Launching One Hybrid (MPI+Threads) Application
-   More Than One Serial Application in the Same Job
-   MPI Applications One at a Time
-   More than One MPI Application Running Concurrently
-   More than One OpenMP Application Running Concurrently

# **Running Jobs**

## **Job Accounting**

The charge unit for *Delta* is the Service Unit (SU). This corresponds
to the equivalent use of one compute core utilizing less than or equal
to 2G of memory for one hour, or 1 GPU or fractional GPU using less than
the corresponding amount of memory or cores for 1 hour (see table
below). *Keep in mind that your charges are based on the resources that
are reserved for your job and don't necessarily reflect how the
resources are used.* Charges are based on either the number of cores or
the fraction of the memory requested, whichever is larger. The minimum
charge for any job is 1 SU.

<table class="wrapped">
<tbody>
<tr class="header">
<th colspan="2"><p>Node Type</p></th>
<th style="text-align: center;" colspan="3">Service Unit
Equivalence</th>
</tr>

<tr class="odd">
  <td colspan="2"></td>
<td>Cores</td>
<td>GPU Fraction</td>
<td style="text-align: center;">Host Memory</td>
</tr>
<tr class="even">
<td colspan="2">CPU Node</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">N/A</td>
<td style="text-align: center;">2 GB</td>
</tr>
<tr class="odd">
<td rowspan="4"><p>GPU Node</p></td>
<td>Quad A100</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1/7 A100</td>
<td style="text-align: center;">8 GB</td>
</tr>
<tr class="even">
<td>Quad A40</td>
<td style="text-align: center;">16</td>
<td style="text-align: center;">1 A40</td>
<td style="text-align: center;">64 GB</td>
</tr>
<tr class="odd">
<td>8-way A100</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1/7 A100</td>
<td style="text-align: center;">32 GB</td>
</tr>
<tr class="even">
<td>8-way MI100</td>
<td style="text-align: center;">16</td>
<td style="text-align: center;">1 MI100</td>
<td style="text-align: center;">256 GB</td>
</tr>
</tbody>
</table>

Please note that a weighting factor will discount the charge for the
reduced-precision A40 nodes, as well as the novel AMD MI100 based node -
this will be documented through the XSEDE SU converter.

### Job Accounting Considerations

-   A node-exclusive job that runs on a compute node for one hour will
    be charged 128 SUs (128 cores x 1 hour)
-   A node-exclusive job that runs on a 4-way GPU node for one hour will
    be charge 4 SUs (4 GPU x 1 hour)
-   A node-exclusive job that runs on a 8-way GPU node for one hour will
    be charge 8 SUs (8 GPU x 1 hour)
-   A shared job that runs on an A100 node will be charged for the
    fractional usage of the A100 (eg, using 1/7 of an A100 for one hour
    will be 1/7 GPU x 1 hour, or 1/7 SU per hour, except the first hour
    will be 1 SU (minimum job charge).

## **Accessing the Compute Nodes**

Describe how to run jobs

-   batch job
-   interactive sessions 
-   ssh from a login node directly to a compute node

## **Job Scheduler**

Describe the job scheduler & scheduling algorithms

Most, if not all, XSEDE resources are running Slurm and this
documentation already exists in some form.

## **Partitions (Queues)**

Describe current partitions.

Table. Delta Production Queues

<table class="wrapped">
<tbody>
<tr class="odd">
<td><p><strong>Queue Name</strong></p></td>
<td><p><strong>Node Type</strong></p></td>
<td><p><strong>Max Nodes per Job</strong></p>
<p><br />
</p></td>
<td><p><strong>Max Duration</strong></p></td>
<td><p><strong>Max Jobs in Queue*</strong></p></td>
<td><p><strong>SU Charge Rate</strong></p>
<p><strong>(per node-hour)</strong></p></td>
</tr>
<tr class="even">
<td><p><span>TBD</span></p></td>
<td><p><span>TBD</span></p></td>
<td><p>TBD</p></td>
<td>TDB</td>
<td><p><span>TDB</span></p></td>
<td><p><span>TBD</span></p></td>
</tr>
</tbody>
</table>

### **Node Policies**

Node-sharing will supported

GPU NVIDIA MIG (GPU slicing) for the A100 will be supported.

## **Interactive Sessions**

Describe any tools for running interactive jobs on the compute nodes.

-   built-in tools for running interactive jobs, e.g. PSC’s interact,
    TACC’s idev

# **Sample Job Scripts (TBD)**

**Sample job scripts are the most requested documentation.**

Provide sample job scripts for common job type scenarios.

-   Serial jobs
-   MPI
-   OpenMP
-   Hybrid (MPI + OpenMP)
-   Parametric / Array / HTC jobs

# **Job Management **

Batch jobs are submitted through a *job script* using
the sbatch command. Job scripts generally start with a series of
SLURM *directives* that describe requirements of the job such as number
of nodes, wall time required, etc… to the batch system/scheduler (SLURM
directives can also be specified as options on the sbatch command line;
command line options take precedence over those in the script). The rest
of the batch script consists of user commands.

The syntax for sbatch is:

**sbatch** \[list of sbatch options\] script\_name

The main sbatch options are listed below.  Refer to the sbatch man page
for options.

-   The common resource\_names are:  
    --time=*time*

    **time**=maximum wall clock time (d-hh:mm:ss) *\[default: maximum
    limit of the queue(partition) summitted to\]*

    --nodes=*n*

    --ntasks=*p* Total number of cores for the batch job

    --ntasks-per-node=*p* Number of cores per node

    n=number of N-core nodes *\[default: 1 node\]*  
    p=how many cores(ntasks) per job or per node(ntasks-per-node) to use
    (1 through 128) *\[default: 1 core\]*

    Examples:  
    --time=00:30:00  
    --nodes=2  
    --ntasks=256  
      
    or  
      
    --time=00:30:00  
    --nodes=2  
    --ntasks-per-node=128  
     

    **Memory:** The compute nodes have at lest 256GB. 

    Example:  
    --time=00:30:00  
    --nodes=2  
    --ntask=256  
    --mem=118000  
      
    or  
      
    --time=00:30:00  
    --nodes=2  
    --ntasks-per-node=64  
    --mem-per-cpu=7375

  

#### **squeue/scontrol/sinfo**

Commands that display batch job and partition information .

<table class="wrapped">
<tbody>
<tr class="header">
<th style="text-align: center;">SLURM EXAMPLE COMMAND</th>
<th style="text-align: center;">DESCRIPTION</th>
</tr>

<tr class="odd">
<td style="text-align: center;"><span style="color: rgb(0,0,0);">squeue
-a</span></td>
<td style="text-align: center;">List the status of all jobs on the
system.</td>
</tr>
<tr class="even">
<td style="text-align: center;"><span style="color: rgb(0,0,0);">squeue
-u $USER</span></td>
<td style="text-align: center;">List the status of all your jobs in the
batch system.</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><span style="color: rgb(0,0,0);">squeue
-j JobID</span></td>
<td style="text-align: center;">List nodes allocated to a running job in
addition to basic information..</td>
</tr>
<tr class="even">
<td style="text-align: center;"><span
style="color: rgb(0,0,0);">scontrol show job JobID</span></td>
<td style="text-align: center;">List detailed information on a
particular job.</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><span style="color: rgb(0,0,0);">sinfo
-a</span></td>
<td style="text-align: center;">List summary information on all the
partition.</td>
</tr>
</tbody>
</table>

See the manual (man) pages for other available options.

  

Useful Batch Job Environment Variables

<table class="relative-table wrapped" style="width: 100.0%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;"><p>DESCRIPTION</p></th>
<th style="text-align: left;"><p>SLURM ENVIRONMENT VARIABLE</p></th>
<th style="text-align: left;"><p>DETAIL DESCRIPTION</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">JobID</td>
<td style="text-align: left;">$SLURM_JOB_ID</td>
<td style="text-align: left;">Job identifier assigned to the job</td>
</tr>
<tr class="even">
<td style="text-align: left;">Job Submission Directory</td>
<td style="text-align: left;">$SLURM_SUBMIT_DIR</td>
<td style="text-align: left;">By default, jobs start in the directory
that the job was submitted from. So the "cd $SLURM_SUBMIT_DIR" command
is not needed.</td>
</tr>
<tr class="odd">
<td style="text-align: left;">Machine(node) list</td>
<td style="text-align: left;">$SLURM_NODELIST</td>
<td style="text-align: left;">variable name that contains the list of
nodes assigned to the batch job</td>
</tr>
<tr class="even">
<td style="text-align: left;">Array JobID</td>
<td style="text-align: left;">$SLURM_ARRAY_JOB_ID<br />
$SLURM_ARRAY_TASK_ID</td>
<td style="text-align: left;">each member of a job array is assigned a
unique identifier</td>
</tr>
</tbody>
</table>

See the sbatch man page for additional environment variables available.

**srun**

The srun command initiates an interactive job on the compute nodes.

For example, the following command:

`srun --time=00:30:00 --nodes=1 --ntasks-per-node=64 --pty /bin/bash`

will run an interactive job in the default queue with a wall clock limit
of 30 minutes, using one node and 16 cores per node. You can also use
other sbatch options such as those documented above.

After you enter the command, you will have to wait for SLURM to start
the job. As with any job, your interactive job will wait in the queue
until the specified number of nodes is available. If you specify a small
number of nodes for smaller amounts of time, the wait should be shorter
because your job will backfill among larger jobs. You will see something
like this:

`srun: job 123456 queued and waiting for resources`

Once the job starts, you will see:

`srun: job 123456 has been allocated resources`

and will be presented with an interactive shell prompt on the launch
node. At this point, you can use the appropriate command to start your
program.

When you are done with your runs, you can use the exit command to end
the job.

**scancel**

The scancel command deletes a queued job or kills a running job.

-   scancel JobID deletes/kills a job.

# **Refunds**

Refunds are considered, when appropriate, for jobs that failed due to
circumstances beyond user control.

XSEDE users and project that wish to request a refund should see the
XSEDE Refund Policy section located
[here](https://portal.xsede.org/su-converter#:~:text=RESET-,XSEDE%20Refund%20Policy,-(v1.2)).

Other allocated users and projects wishing to request a refund
should email <help@ncsa.illinois.edu>. Please include the batch job ids
and the standard error and output files produced by the job(s). 

# **Visualization**

Delta A40 nodes support NVIDIA raytracing hardware.

-   describe visualization capabilities & software.
-   how to establish VNC/DVC/remote desktop

# **Containers**

Delta will support container use with Singularity.

NVIDIA NGC containers will be made available. 

# **Protected Data (N/A)**

IF APPLICABLE

-   Describe the system’s capabilities for handling protected data.
-   Data Retention Policies
-   How to run jobs with protected data.
-   Describe any mandated workflows.

# **Help**

For assistance with the use of Delta

-   XSEDE users can create a ticket via the user portal at
    <https://portal.xsede.org/web/xup/help-desk>
-   All other users (Illinois allocations, Diversity Allocations, etc)
    please send email to help@ncsa.illinois.edu.

# **Acknowledge**

To acknowledge the NCSA Delta system in particular, please include the
following

This research is part of the Delta research computing project, which is
supported by the National Science Foundation (award OCI 2005572), and
the State of Illinois. Delta is a joint effort of the University of
Illinois at Urbana-Champaign and its National Center for Supercomputing
Applications.

To include acknowledgement of XSEDE contributions to a publication or
presentation please see <https://portal.xsede.org/acknowledge> and
<https://www.xsede.org/for-users/acknowledgement>.

# **References**

List any supporting documentation resources

  

