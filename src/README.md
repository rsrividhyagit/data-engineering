# DATA ENGINEERING TEST

> This is to illustrate different coding practices and modular design limited to the context of the problem statement.
> > The code is documented without the need to read the following.


## Requirements
* Python 3.7*




## Standards Followed(Prominent)

* PEP 8
    > Naming Conventions, Line Lengths
* [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
    > This Docstring Style can be changed to any other or custom too.
* PEP 484 - Type Hinting
* Other PEP Standards
* Reduced Cognitive Complexity - Concise Functions 


## Notes

* **SOURCECOLUMNS.txt** file is assumed to be always smaller is size and is handled without any buffer. 
* **SOURCEDATA.txt** file is assumed to be large and can be handled using chunk sizes, but prefer using pandas.read_csv() if we are allowed to use libraries.
* Some functions are written only to show Re-Usability of code, but no really necessary.
* If the functions are to be used with timeit with a larger dataset, please consider the **data is also sorted by Order Id** which is **not** in the Problem Statement.
* There is always room for Improvement, better documentation and Testing Coverage, in this context and the timeframe this is what's done so far.
