# calc ekf_localizer delay average

calc delay time of ekf_localizer using diagnostics

## Prerequisites

- [Autoware](https://github.com/autowarefoundation/autoware) main
- Python 3.10

## Usage

1. run Autoware
2. ros2 topic echo /diagnostics
3. copy displayed log in your terminal as yaml file
4. replace lidar_name (analyzer.py line 33)
5. run analyer.py
