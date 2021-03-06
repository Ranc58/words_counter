Words in names counter
===========================

| This script calculate words count (nouns and verbs) in funcs and vars names in ``.py`` files.
| Script check all folders recursively.
| Script can clone repo from github&


How to install
==============

| Run ``pip3 install words_counter``
| Run on CLI for update nltk if it need:\

::

    $ python3
    >> import nltk
    >> nltk.download('all')

How to use
==========

| Script have some arguments to run:
| ``-p`` - Projects dirpathes.
| ``--all_names`` - Get all vars and funcs names.
| ``--by_type`` - Get all info by word type.
| ``--top_names`` - Get top funcs and vars names.
| ``-d`` - Clone code from outsource(Github in this version, need repo URL and pathway to create folder)
| ``-t`` - Add word type for search. Avaliable types: NN(Noun), NNS(Nouns), VB(Verb).
| ``--data_type`` - Structure to search choice. Available funcs or vars.
| ``--cli`` - Output result to CLI.
| ``--json`` - Output result to JSON file(need pathway to create json file).
| ``--csv`` - Output result to CSV file(need pathway to create csv file).
| `Attention!` In current version ``-t`` and ``--data_type`` required, only if you don't want use ``-d``.

Usage example:
==============

We have some folders structure with ``dclint.py``:

::

    ├── dclint.py
    ├── django
    │   ├── css
    │   ├── bootstrap.min.css
    │   ├── my_app.py
    │
    ├── flask
    │   ├── favicon.ico
    │   ├── polls.py
    │   ├── garbage_files
    │   │   ├──bootstrap.min.js
    │   │   ├──html5shiv.min.js
    │   │   ├──thrash.py
    │
    ├── myproject
    │   ├──ie-emulation-modes-warning.js
    │   ├──old_version.py
    │   ├──new_file.py

| In all folders - 5 ``.py`` files.\
| All files have funcs like this (for example):

::

    def foo():
       test_var1 = 'test'
       return test_var1


::

    def bar():
        test_var2 = 'haha'
        return test_var2

::

    if __name__ == '__main__':
        foo_var = foo()
        bar_var = bar()


And another funcs.

| Run check(for example from project folder):\
| ``$ python words_counter -p myproject -t vb --data_type funcs --all_names --cli``\
| Result:

::

    project: myproject
    funcs names:
            foo
            bar
    vars names:
            test_var1
            test_var2
            foo_var
            bar_var


License
=======

MIT license
