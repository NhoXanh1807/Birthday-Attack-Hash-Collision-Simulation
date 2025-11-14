"""
Logging utilities for simulation experiments.
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


class SimulationLogger:
    """Logger for recording simulation experiments."""

    def __init__(self, log_dir: str = "results/logs"):
        """
        Initialize logger.

        Args:
            log_dir: Directory to store log files
        """
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = self.log_dir / f"simulation_{self.session_id}.log"
        self.json_file = self.log_dir / f"simulation_{self.session_id}.json"
        self.experiments = []

    def log(self, message: str):
        """Write a log message."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] {message}\n"

        with open(self.log_file, 'a') as f:
            f.write(log_line)

        print(log_line.strip())

    def record_experiment(self, experiment_data: Dict[str, Any]):
        """
        Record an experiment with its parameters and results.

        Args:
            experiment_data: Dictionary containing experiment details
        """
        experiment_data['timestamp'] = datetime.now().isoformat()
        self.experiments.append(experiment_data)

        # Save to JSON
        with open(self.json_file, 'w') as f:
            json.dump({
                'session_id': self.session_id,
                'experiments': self.experiments
            }, f, indent=2)

        self.log(f"Recorded experiment: {experiment_data.get('name', 'Unknown')}")

    def get_summary(self) -> str:
        """Get a summary of all logged experiments."""
        summary = []
        summary.append(f"Session ID: {self.session_id}")
        summary.append(f"Total Experiments: {len(self.experiments)}")
        summary.append(f"Log File: {self.log_file}")
        summary.append(f"Data File: {self.json_file}")
        return "\n".join(summary)


def create_experiment_report(
    experiment_name: str,
    parameters: Dict[str, Any],
    results: Dict[str, Any],
    output_file: str = None
) -> str:
    """
    Create a formatted experiment report.

    Args:
        experiment_name: Name of the experiment
        parameters: Experiment parameters
        results: Experiment results
        output_file: Optional file to save report

    Returns:
        Formatted report string
    """
    report_lines = []
    report_lines.append("=" * 70)
    report_lines.append(f"EXPERIMENT REPORT: {experiment_name}")
    report_lines.append("=" * 70)
    report_lines.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("")

    report_lines.append("PARAMETERS:")
    report_lines.append("-" * 70)
    for key, value in parameters.items():
        report_lines.append(f"  {key}: {value}")
    report_lines.append("")

    report_lines.append("RESULTS:")
    report_lines.append("-" * 70)
    for key, value in results.items():
        report_lines.append(f"  {key}: {value}")
    report_lines.append("")

    report_lines.append("=" * 70)

    report_text = "\n".join(report_lines)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(report_text)
        print(f"Report saved to {output_file}")

    return report_text
