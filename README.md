#  INSC712 Forensic Analysis Project
## Using Wireshark and Tcpdump to Detect ARP Poisoning and Man-in-the-Middle Attacks
### 2023 Fall Group 16: Nora Liu, Parker Cheng, Yousef Alawamleh

## Project Introduction
This forensic investigation analyzes a substantial breach in business confidentiality involving Company A and its manufacturing partner, Company B. The exposure of critical information, encompassing essential details like product design, target market, manufacturing specifics, production costs, and retail prices, unfolded ahead of Company A's official product launch. Notably, Company M, a competitor, swiftly released a product mimicking Company A's design, implying a potential information leak. Commissioned by both entities, our forensic specialists employed Wireshark and Tcpdump forensic tools, uncovering ARP cache poisoning within the same LAN and implicating an intruder associated with a suspect employee. Subsequent interviews authenticated the employee's involvement, revealing the unauthorized removal and utilization of a confidential device outside of office, where malicious software was installed in confidential devices. The findings lights the urgency for robust cybersecurity protocols. However, this investigation grapples with certain limitations, prompting recommendations for alternative forensic tools such as Bro (Zeek) and NetworkMiner, the implementation of countermeasures, and thoughtful consideration of factors like realism and legal considerations related to evidence captured using Wireshark and Tcpdump. The research provides crucial insights to enhance organizational cybersecurity, facilitating potential advancements in the field of digital forensics.

This Attack is based on the following topology: 

<img src="attack_topology" alt="Attack Topology" width="400"/>

The summary table Hosts and their MAC address and IP address are listed in the following table:

<img src="summary_MAC_IP_table" alt="Summary of MAC and IP Address of Related Parties" width="400"/>


## Table of Contents

- Related code
- [Manual of how to conduct the MITM attack using ARP Posioning] [712_ARP_manual.pdf]
- Reference 

## Related Code 

Explain how someone can get started with your project. Include any prerequisites they need to install and instructions for installation.

```bash
# Example installation command
npm install
```
## Manual of how to conduct the Attack


## Reference
The attack process is referenced based on SEEDLabs retrived from: 
SEEDLabs. (2023). ARP Cache Poisoning Lab. Syracuse University. https://seedsecuritylabs.org/Labs_20.04/Networking/ARP_Attack/



