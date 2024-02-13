Documentation Demo
==================

This is a demo page to show how to use Readthedocs to automatically generate documentation website based on your **python** code. Other code such as *Arduino*, *C++* should also be supported but needs to be tested.

Readthedocs automatically pulls docstring from your code file. Some useful tutorials can be found `here <https://docs.readthedocs.io/en/stable/tutorial/index.html>`_, `here <https://pythonforthelab.com/blog/documenting-with-sphinx-and-readthedocs/>`_, and `here <https://amazonwebshark.com/open-source-documentation-with-read-the-docs/>`_.

Different from GitHub, Readthedocs uses reStructuredText (``.rst`` format, instead of ``.md`` format of Markdown) for plain text markup. Here are some cheat sheets of the ``.rst`` format are as below:

* https://docs.anaconda.com/restructuredtext/index.html
* https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
* https://sphinx-tutorial.readthedocs.io/cheatsheet/

This demonstrates the page reference function: :doc:`factorial` and :doc:`people`. 

Setup
-----

#. Register an account on https://readthedocs.org/. In the ``Settings`` page, connect your GitHub account.

   .. image:: /img/readthedocs_setting_page.png
      :align: left

#. Clone this repo () to your local PC.

.. note::

   This project is under active development as of 02/13/2024.
   
   Build ver: 8

Contents
--------

.. toctree::
    :caption: Contents:

    factorial
    people