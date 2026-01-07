# Linux Resource Logger Service 🐧

A lightweight Linux background service (Daemon) that monitors system resources. It automatically logs the top CPU-consuming processes every 2 seconds to a persistent log file.

This project demonstrates how to build custom system services using **Python** and **Systemd**.

* **Real-time Monitoring:** Captures CPU and Memory usage snapshots every 2 seconds.
* **Process Tracking:** Identifies the specific command and PID causing load.
* **Background Execution:** Runs silently as a Daemon using `systemd`.
* **Resilience:** Automatically restarts if the script crashes or the system reboots.

## Working
1.  **The Engine (`monitor.py`):** A Python script that executes Linux commands (`ps`) to fetch system data and appends it to a log file.
2.  **The Controller (`systemd`):** A unit file that manages the lifecycle of the Python script (Start, Stop, Restart, Boot logic).

>  This project was developed for for personal understanding of how linux systems work, services, permissions and more.
