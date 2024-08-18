publish:
    pdm build
    twine upload dist/*

test:
    pdm run pytest tests/