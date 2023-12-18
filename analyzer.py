#!/usr/bin/env python3

import yaml
from pathlib import Path


def main(input_pointcloud: str):
    total_valid_ekf_localizer = 0
    sum_pose_delay_time = 0.0
    sum_twist_delay_time = 0.0
    with Path(__file__).parent.joinpath(input_pointcloud + ".yaml").open() as f:
        diagnostics = yaml.safe_load_all(f)
        for diag in diagnostics:
            diag: dict
            for k, v in diag.items():
                v: list[dict]
                if k == "status" and v[0]["name"] == "localization: ekf_localizer" and v[0]["message"] == "OK":
                    total_valid_ekf_localizer += 1
                    for key_value in v[0]["values"]:
                        if key_value["key"] == "pose_delay_time":
                            sum_pose_delay_time += float(key_value["value"])
                        if key_value["key"] == "twist_delay_time":
                            sum_twist_delay_time += float(key_value["value"])
    average_pose_delay_time = sum_pose_delay_time / total_valid_ekf_localizer
    average_twist_delay_time = sum_twist_delay_time / total_valid_ekf_localizer
    with Path(__file__).parent.joinpath(input_pointcloud + "_result.txt").open("w") as fo:
        fo.write(f"{total_valid_ekf_localizer=}\n")
        fo.write(f"{average_pose_delay_time=}\n")
        fo.write(f"{average_twist_delay_time=}\n")


if __name__ == "__main__":
    main("concatenated")
