# Finance Advisor

A system to help with financial decisions.

## Setup

This project uses Poetry for dependency management. To get started:

1. Make sure you have Poetry installed
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Project Structure

```
finance-advisor/
├── src/                    # Source code
│   └── finance_advisor/    # Main package
├── tests/                  # Test files
├── pyproject.toml         # Poetry configuration
└── README.md              # This file
```

## Development

To run the application:
```bash
poetry run python -m src.finance_advisor.main
```

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). 