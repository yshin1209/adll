# adll
# Adaptive-Deep-Learning-Library

# pythong.org - Packaging Python Projects
# https://packaging.python.org/en/latest/tutorials/packaging-projects/

# Create a PyPI (pip) package, test it and publish it using Github Actions
# https://dev.to/arnu515/create-a-pypi-pip-package-test-it-and-publish-it-using-github-actions-part-1-3cp8


# testpypi upload
# id __token__
# pw: pypi-AgENdGVzdC5weXBpLm9yZwIkMzcxM2I1OTktOGZkYy00MGFhLWFiYmUtYjNlM2UwODQzYThhAAIqWzMsIjg5YjEyYzA0LTMwNzYtNGIyYS05NDJmLThlMDM3NzYxODM1NiJdAAAGIGYc9ZS3eGgmmFQf4yPj_yyR0V1gKeziiCQ9xqHUZEsq
# py -m build
# py -m twine upload --repository testpypi dist/*