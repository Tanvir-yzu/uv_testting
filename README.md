# UV Project

A Python project managed with UV package manager.

## Prerequisites

- [UV](https://docs.astral.sh/uv/) package manager installed
- Python 3.12+ (managed by UV)

## Getting Started

### 1. Install UV

If you don't have UV installed:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd uv

# Create virtual environment and install dependencies
uv sync
```

### 3. Running the Project

```bash
# Run the main script
uv run python main.py

# Run any Python command in the virtual environment
uv run python -c "print('Hello World')"

# Run Python interactively
uv run python
```

## Project Structure

```
uv/
├── .venv/                 # Virtual environment (auto-managed by UV)
├── .python-version        # Python version specification
├── pyproject.toml         # Project configuration and dependencies
├── uv.lock               # Lock file for reproducible builds
├── main.py               # Main application entry point
└── README.md             # This file
```

## Development

### Adding Dependencies

```bash
# Add a production dependency
uv add requests

# Add a development dependency
uv add --dev pytest

# Add from requirements.txt
uv add -r requirements.txt
```

### Running Tests

```bash
# If you have pytest installed
uv run pytest

# Run with coverage
uv run pytest --cov
```

### Python Version Management

```bash
# Set Python version for this project
uv python pin 3.12

# Use a specific Python version
uv run --python 3.11 python main.py
```

## Available Scripts

The following commands are available:

- `uv run python main.py` - Run the main application
- `uv sync` - Install/update dependencies
- `uv lock` - Update the lock file
- `uv tree` - Show dependency tree
- `uv python --version` - Show Python version

## Environment Variables

You can create a `.env` file for environment variables:

```bash
# Create .env file
echo "DEBUG=true" > .env
echo "API_KEY=your-api-key" >> .env
```

Load environment variables in your Python code:

```python
import os
from pathlib import Path

# Load .env file if it exists
env_file = Path('.env')
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value
```

## Troubleshooting

### Common Issues

1. **UV not found**: Make sure UV is installed and in your PATH
2. **Permission errors**: Run `uv venv --refresh` to recreate the virtual environment
3. **Import errors**: Run `uv sync` to ensure all dependencies are installed

### Useful Commands

```bash
# Check UV version
uv --version

# Show project information
uv python list
uv pip list

# Clean and recreate virtual environment
uv venv --refresh

# Clear UV cache
uv cache clean
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests with `uv run pytest` (if tests exist)
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [PEP 621 - Project Metadata](https://peps.python.org/pep-0621/)