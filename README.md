# User Behavior Analytics Pipeline

A Python pipeline for processing event-level user data and generating daily product metrics.

## Overview

This project simulates a simple analytics workflow commonly used in product or data teams:

* Generate synthetic user event data
* Calculate daily KPIs from raw events
* Export results for downstream analysis

The goal is to demonstrate clean project structure, basic data processing logic, and reproducible workflow using Python.

## Features

* Synthetic event data generation
* Daily KPI calculation:

  * DAU (Daily Active Users)
  * Purchasers
  * Revenue
  * Conversion rate
* CSV output for analysis or reporting

## Project Structure

```
user-behavior-analytics/
├── main.py                 # Pipeline entry point
├── scripts/
│   └── make_data.py        # Synthetic data generation
├── src/
│   └── metrics.py          # KPI calculation logic
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:ruizhw19/user-behavior-analytics.git
cd user-behavior-analytics
```

### 2. Set up environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Run the pipeline

```bash
python main.py
```

Generated output will be saved to the `output/` folder.

## Notes

* The dataset is synthetic and used only for demonstration.
* `data/` and `output/` folders are excluded from version control to keep the repository lightweight.

## Skills Demonstrated

* Python scripting
* Data processing workflow design
* Analytics metric calculation
* Clean project organization
