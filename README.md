# Challenges mix

[![Python Version][python-image]][python-url]

Challenges successfully accomplished!

## Installation

### Environment Local

We use python 3.10 for all challenges, so just choose your dependency manager, create a python environment, follow a [link](https://ahmed-nafies.medium.com/pip-pipenv-poetry-or-conda-7d2398adbac9) talking about the managers!

Access the project folder and using the **pip** manager, inside the python env, apply the command below:

Upgrade pip version and install requirements and install:

```sh
pip install --upgrade pip && pip install --require-hashes -r requirements.txt
```

## Usage

After installing all dependencies,compile this project with command:

```sh
python scripts/<module_name>.py <input_date>
```

**Obs:**

* It depends on the module, the input quantity changes, you need to check it first!

### Formatters and Linters

* [Flake8](https://flake8.pycqa.org/en/latest/index.html)
* [Black](https://black.readthedocs.io/en/stable/)
* [Isort](https://isort.readthedocs.io/en/latest/)
* [MyPy](https://mypy.readthedocs.io/en/stable/)

**Obs:**

* Programming with python, we use the **snake case style**.

### Structure

We based on **Serveless architecture patterns**, to create theses resources. See the content:


```sh
.
├── artifacts
│   ├── answers.txt
│   └── LeanonSystems_Logicsandprogramming.pdf
├── pyproject.toml
├── README.md
├── requirements.in
├── requirements.txt
├── scripts
│   ├── __init__.py
│   ├── paint_bucket_tool.py
│   ├── palindrome.py
│   ├── phonebook.py
│   └── supplier_query.sql
└── tests
    ├── __init__.py
    ├── test_paint_bucket_tool.py
    ├── test_palindrome.py
    └── test_phonebook.py
```

### Tests

In this application, we used this dependencies to perform, scan and cover tests in the application:

* [Pytest](https://docs.pytest.org/en/6.2.x/)

In this application, unit tests were created, using **pytest**. Follow the instructions to run the tests:

* To see tests list and your tests cases

```sh
pytest --co
```

* To run all test

```sh
pytest tests/
```

* To run only test module

```sh
pytest tests/<module_name>.py
```

* To run only function test module

```sh
pytest tests/<module_name>.py::<function_teste_name>
```

## Tips

In this session, we include several articles related to good practices, tools and more.

* [Tips for pip-tools and multple environments](https://www.caktusgroup.com/blog/2018/09/18/python-dependency-management-pip-tools/)
* [Locking dependency with pip-tools](https://lincolnloop.com/blog/python-dependency-locking-pip-tools/)
* [Tips for environments python](https://towardsdatascience.com/virtual-environments-104c62d48c54)
* [SOLID Principle](https://medium.com/@engnogueirawgn/princ%C3%ADpios-solid-na-pr%C3%A1tica-e932608406d6)
* [Clean Code and principles](https://henriquesd.medium.com/dry-kiss-yagni-principles-1ce09d9c601f)
* [Environments python, what is have choosen?](https://ahmed-nafies.medium.com/pip-pipenv-poetry-or-conda-7d2398adbac9)
* [Overview of python dependency management tools](https://modelpredict.com/python-dependency-management-tools)
* [Types of development styles](https://betterprogramming.pub/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841)
* [Best pratices in Python](https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5?gi=6989d5c08d78)
* [Flake 8 best configurations](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html)
* [Black tips](https://www.mattlayman.com/blog/2018/python-code-black/)
* [EditorConfig tips](https://blog.matheuscastiglioni.com.br/padronizando-seus-editores-de-texto-com-editorconfig/)

## Resources and Documentations

* [Pip (Package Installer Python)](https://pip.pypa.io/en/stable/)
* [Editor Config](https://editorconfig.org/)
* [Pip Tools](https://github.com/jazzband/pip-tools)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

[python-url]: https://www.python.org/dev/peps/pep-0596/
[python-image]: https://img.shields.io/badge/python-v3.10-blue
