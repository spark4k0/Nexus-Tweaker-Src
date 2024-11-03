# Nexus Tweaker Source Code Repository

Welcome to the **Nexus Tweaker Source Code** repository! This README provides an overview of the story behind Nexus Tweaker, details about the code and its contents, and opinions on both the owner and PC tweakers in general. This guide is structured to be clear and informative, so you know exactly where to find everything. 🛠️

---

## 📜 Story

### Background
The owner of this project, **thorstellini** (Discord user ID: `1230775914099376240`), created a server called **Nexus Tweaks**, where he sells a PC tweaker utility. In addition to the paid version, there is a **free "beta" version** with limited features, offering only basic Windows tweaks that aren’t particularly useful.

### Discovery
A friend (or possibly an alternate account) promoted Nexus Tweaks on **Amar's Discord server** (`discord.gg/amar`). After joining to investigate, the project initially seemed legitimate. However, after discovering a free trial version and analyzing the content, suspicions grew about the tool's authenticity.

### Analysis
The **free beta version** was analyzed using [tria.ge](https://tria.ge) to check for malicious content (analysis report [here](https://tria.ge/241102-r9gl3sxenq/behavioral1)). No suspicious elements were detected, so the tool was downloaded on a virtual machine for further inspection. Surprisingly, there were **no external connections** to validate the license key, indicating the entire validation is handled locally with the code-stored license `FREE-XXXX-XXXX-XXXX`.

The **decompiled and extracted source code** from this tool is provided in this repository in separate folders for easier navigation.

---

## 📂 Repository Structure

### Code Structure
The repository contains the decompiled and extracted code of Nexus Tweaker, split into separate folders:
- **Decompiled Code**: Contains all available decompiled files.
- **Extracted Files**: Holds any non-decompiled .pyc files that you can explore further if desired.

### Important Note
There is a significant amount of redundant and poorly optimized code, with many repeating functions. **Support for this code will not be provided.** You are welcome to analyze, modify, or use it as you see fit. Be aware of any **potentially harmful commands**, especially PowerShell scripts, which might corrupt your system if misused.

---

## ⚠️ Disclaimer & Warnings

- **Potential Risks**: Some functions in the code, particularly PowerShell commands, could damage your system if mishandled. Always review the code you execute.
- **No Guarantees**: The source code is offered as-is, with no guarantees or support.

---

## 🔍 Final Opinions

### On Nexus
The owner of Nexus Tweaks appears to lack technical depth, evidenced by his use of a bot hosting service, **Bot Ghost**, to host "Nexus Bot" (#3221, Discord user ID: `1295367068123926558`). A competent developer could easily create and host a Discord bot for free on a Python hosting service, underscoring a lack of basic understanding.

### On PC Tweakers
In general, **PC tweakers are not recommended**. These tools often overpromise and underdeliver, and the performance improvements they claim can typically be achieved more effectively by:
- Using a custom Windows OS (e.g., **Ghost Spectre**)
- Making BIOS adjustments (with caution)
  
Always ensure that you understand the changes you're making, especially when altering system configurations.

---

## 📄 License

This repository is public domain. You are free to use, modify, and redistribute the code as you wish.

---

## 📬 Contact

Feel free to reach out on Discord (spark4k) if you have any questions (although no support will be provided for this codebase). 

---

Enjoy exploring the Nexus Tweaker code! Be cautious, and remember that true performance improvements are often found outside of these kinds of tools. 🚀
