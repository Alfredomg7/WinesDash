# Wines Dash App

Dash app that visualizes and compares a dataset of PDO wines from France and Italy. 

---

## Features

- **Wine Color Distribution**: Visualize the distribution of wine colors (Red, White, Rosé) across countries.
- **Registration Trends**: Analyze the trend of wine registrations over time for France and Italy.
- **Interactive Filter**: Filter charts by specific wine categories.
- **Responsive Layout**: Designed with Dash Bootstrap Components for a responsive and user-friendly UI.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.8+
- pip (Python package manager)

### Installation

Clone the repository:

```bash
git clone https://github.com/Alfredomg7/WinesDash.git
cd wines-dash
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the dataset:

```bash
python init_db.py
```

Run the application:

```bash
python app.py
```

Open the app in your web browser at:

http://127.0.0.1:8050

## Acknowledgements

- The dataset used in this application is sourced from the [ScienceDirect PDO Wine Dataset](https://www.sciencedirect.com/science/article/pii/S2352340924003779).