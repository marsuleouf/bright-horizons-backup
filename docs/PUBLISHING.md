# Publishing to PyPI

This guide walks you through publishing the Bright Horizons Backup package to PyPI.

## Project Structure

```
src/bright_horizons_backup/
├── __init__.py          # Package initialization
├── cli.py              # Command-line interface  
├── client.py           # Main client class
├── models.py           # Data models
├── auth.py             # Authentication logic
├── api_client.py       # API interactions
├── browser_utils.py    # Browser automation
├── constants.py        # Configuration constants
├── utils.py            # Utility functions
├── viewer.py           # Web viewer
└── templates/          # HTML templates
```

## Prerequisites

1. **PyPI Account**: Create accounts on both [PyPI](https://pypi.org) and [TestPyPI](https://test.pypi.org)

2. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **API Tokens**: Generate API tokens for both PyPI and TestPyPI:
   - Go to Account Settings → API tokens
   - Create a token with appropriate scope
   - Add `PYPI_API_TOKEN` to GitHub repository secrets

## Configuration

### Option 1: Using .pypirc file

Create `~/.pypirc`:
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-test-api-token-here
```

### Option 2: Environment Variables

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-your-api-token-here
```

## Publishing Methods

### Method 1: Automated (Recommended)

1. **Prepare for Release**:
   ```bash
   # Update version in pyproject.toml
   # Update CHANGELOG.md
   # Run tests
   tox
   ```

2. **Create GitHub Release**:
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```
   
3. **Create Release on GitHub**:
   - Go to GitHub → Releases → Create new release
   - Select the tag you just pushed
   - Add release notes
   - Publish release
   
4. **Automatic Publishing**:
   - GitHub Actions will automatically build and publish to PyPI
   - Monitor the "Publish" workflow in Actions tab

### Method 2: Manual

1. **Test Locally**:
   ```bash
   # Run full test suite
   uv run tox
   
   # Build package
   uv build
   ```

2. **Test on TestPyPI**:
   ```bash
   uv publish --publish-url https://test.pypi.org/legacy/
   pip install --index-url https://test.pypi.org/simple/ bright-horizons-backup
   ```

3. **Publish to PyPI**:
   ```bash
   uv publish
   ```

## Using the Publish Script

The repository includes a convenience script:

```bash
./scripts/publish.sh
```

This script:
1. Cleans previous builds
2. Builds the package
3. Checks the package with twine
4. Uploads to PyPI

## Package Structure Verification

Before publishing, verify your package structure:

```
bright-horizons-backup/
├── src/
│   └── bright_horizons_backup/
│       ├── __init__.py
│       ├── cli.py
│       ├── viewer.py
│       ├── client.py
│       ├── models.py
│       ├── auth.py
│       ├── api_client.py
│       ├── browser_utils.py
│       ├── constants.py
│       ├── utils.py
│       └── templates/
├── pyproject.toml
├── README.md
├── LICENSE
├── CHANGELOG.md
└── MANIFEST.in
```

## Version Management

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backward-compatible functionality
- **PATCH** version for backward-compatible bug fixes

Examples:
- `1.0.0` → `1.0.1` (bug fix)
- `1.0.1` → `1.1.0` (new feature)
- `1.1.0` → `2.0.0` (breaking change)

## Release Checklist

### Pre-Release
- [ ] Version updated in `pyproject.toml`
- [ ] `CHANGELOG.md` updated with release notes
- [ ] All tests passing (`tox`)
- [ ] Documentation updated
- [ ] Code formatted (`black`, `isort`)
- [ ] Linting passes (`flake8`, `mypy`)

### Release Process
- [ ] Git tag created (`git tag v1.0.1`)
- [ ] Tag pushed to GitHub (`git push origin v1.0.1`)
- [ ] GitHub release created with notes
- [ ] GitHub Actions publish workflow completed
- [ ] Package available on PyPI
- [ ] Installation verified (`pip install bright-horizons-backup`)

### Post-Release
- [ ] Version bump for next development cycle
- [ ] Update documentation if needed

## Troubleshooting

### Common Issues

1. **"File already exists" error**:
   - You're trying to upload a version that already exists
   - Increment the version number

2. **Authentication errors**:
   - Check your API token
   - Ensure token has correct permissions
   - Verify `.pypirc` configuration

3. **Package validation errors**:
   - Run `twine check dist/*` to identify issues
   - Check `pyproject.toml` configuration
   - Ensure all required files are included

### Build Issues

```bash
# Build and check package
uv build
tar -tzf dist/bright-horizons-backup-*.tar.gz

# Test installation locally
uv pip install dist/bright-horizons-backup-*.whl

# Run quality checks
uv run tox -e lint
```

## Security Notes

- Never commit API tokens to version control
- Use environment variables or `.pypirc` for credentials
- Regularly rotate API tokens
- Use scoped tokens with minimal required permissions

## GitHub Actions Integration

This project includes automated workflows:

### Test Workflow (`.github/workflows/test.yml`)
- Runs on every push and PR
- Tests across Python 3.8-3.12
- Generates coverage reports
- Uploads to Codecov

### Publish Workflow (`.github/workflows/publish.yml`)
- Triggers on GitHub releases
- Builds and publishes to PyPI automatically
- Uses `PYPI_API_TOKEN` secret

### Setup GitHub Secrets

1. Go to repository Settings → Secrets and variables → Actions
2. Add `PYPI_API_TOKEN` with your PyPI API token
3. Workflows will use `UV_PUBLISH_TOKEN` environment variable

## Package Features

Once published, the package provides:

- **Backup CLI**: `bright-horizons-backup`
- **Web viewer**: `bright-horizons-viewer` (requires `[viewer]` extra)
- **Python module**: `python -m bright_horizons_backup`
- **Importable library**: `from bright_horizons_backup import BrightHorizonsClient`
- **Cross-platform**: Windows, macOS, Linux support