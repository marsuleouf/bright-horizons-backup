# Contributing to Bright Horizons Backup

Thank you for your interest in contributing to Bright Horizons Backup! This document provides guidelines for contributing to the project.

## Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bright-horizons-backup.git
   cd bright-horizons-backup
   ```

2. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # Or: pip install uv
   ```

3. **Install development dependencies**:
   ```bash
   uv sync --extra dev --extra viewer
   playwright install chromium
   ```

4. **Setup pre-commit hooks** (optional but recommended):
   ```bash
   uv run pre-commit install
   ```

## Code Style

This project uses several tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting  
- **flake8** for linting
- **mypy** for type checking

All configuration is in `pyproject.toml`.

```bash
# Format code
uv run black src tests
uv run isort src tests

# Check formatting
uv run black --check src tests
uv run isort --check-only src tests

# Lint and type check
uv run flake8 src tests
uv run mypy src

# Run all quality checks
uv run tox -e lint

# Run security checks
uv run tox -e security

# Or use pre-commit for all checks
uv run pre-commit run --all-files
```

## Testing

This project uses pytest with comprehensive test coverage:

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov --cov-report=html

# Run tests across all Python versions
uv run tox

# Run specific test environments
uv run tox -e py311        # Test on Python 3.11
uv run tox -e cov          # Coverage report
uv run tox -e lint         # Code quality checks
```

### Writing Tests

- Place tests in the `tests/` directory
- Use `test_*.py` naming convention
- Mock external dependencies (httpx, playwright)
- Use async fixtures for async code
- Add integration tests with `@pytest.mark.integration`

## Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Add tests** for new functionality

4. **Update documentation** if needed

5. **Run the test suite**:
   ```bash
   # Quick test
   uv run pytest
   
   # Full test suite
   uv run tox
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

## Commit Message Guidelines

Use conventional commit messages:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

Examples:
- `feat: add support for custom batch sizes`
- `fix: handle network timeouts gracefully`
- `docs: update installation instructions`

## Pull Request Process

1. **Update documentation** for any new features
2. **Add tests** that cover your changes
3. **Ensure all tests pass** and code follows style guidelines
4. **Update CHANGELOG.md** with your changes
5. **Submit a pull request** with a clear description

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] Tests pass locally
- [ ] Added tests for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
```

## Release Process

1. **Update version** in `pyproject.toml`
2. **Update CHANGELOG.md** with release notes
3. **Create a release tag**:
   ```bash
   git tag -a v1.0.1 -m "Release v1.0.1"
   git push origin v1.0.1
   ```
4. **Build and publish**:
   ```bash
   ./scripts/publish.sh
   ```

## Reporting Issues

When reporting issues, please include:

- **Python version** and operating system
- **Package version** you're using
- **Complete error message** and stack trace
- **Steps to reproduce** the issue
- **Expected vs actual behavior**

## Security Issues

For security-related issues, please email the maintainers directly rather than opening a public issue.

## Code of Conduct

This project follows a simple code of conduct:

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain a welcoming environment

## Security

This project includes automated security scanning:

```bash
# Run security checks
uv run bandit -r src/
uv run safety check

# Or use tox
uv run tox -e security
```

## Automated Quality Checks

- **Dependabot** - Automated dependency updates
- **Pre-commit hooks** - Code quality on every commit
- **GitHub Actions** - CI/CD with testing and security scans
- **Coverage reporting** - Codecov integration

## Questions?

If you have questions about contributing, feel free to:

- Open an issue for discussion
- Contact the maintainers
- Check existing issues and pull requests

Thank you for contributing!